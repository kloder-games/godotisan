"""The build command."""

import os

from godotisan.libs.scons import Scons
from godotisan.libs.gradle import Gradle
from godotisan.libs.actions import Actions

import godotisan.utils.files as Files

from .base import Base

class Build(Base):
    """Build the Godot project"""

    DEVNULL = open(os.devnull, 'wb')
    actions = None
    godotmodules_dir = ''
    modules_dir = ''
    module_dir = ''

    def run(self):
        cores = 0
        stdout = None

        if self.options['--cores']:
            cores = int(self.options['--cores'])

        self.actions = Actions()
        scons = Scons(cores, stdout)
        gradle = Gradle(stdout)

        if self.options['godot']:
            scons.build_godot()
            print 'Godot build successfuly!'

        elif self.options['android']:
            print '>>>>>> Installing modules... '
            self.actions = Actions()
            self.godotmodules_dir = os.path.join(os.getcwd(), 'godot/modules')
            self.modules_dir = os.path.join(os.getcwd(), 'modules')
            for module in self.config.get_modules():
                self.module_dir = os.path.join(self.modules_dir, module['id'])
                self.uninstall_module(module)
                self.install_module(module)
            
            print '>>>>>> Processing before build rules... ',
            if self.config.get_actions('before-build') != None:
                self.actions.do_actions(self.config.get_actions('before-build'))
            if self.config.is_firebase():
                if self.config.get_actions('before-build-firebase') != None:
                    self.actions.do_actions(self.config.get_actions('before-build-firebase'))

            print '>>>>>> Cleaning builds... '
            gradle.clean()

            if self.options['--only-debug']:
                print '>>>>>> Building debug template... '
                scons.build_android_debug()
            elif self.options['--only-release']:
                print '>>>>>> Building release template... '
                scons.build_android_release()
            else:
                print '>>>>>> Building release & debug template... '
                scons.build_android_release()
                gradle.build()
                gradle.clean()
                scons.build_android_debug()
            gradle.build()
            print '>>>>>> Process finished!'

    def install_module(self, module):
        """ Install a module """
        if not module:
            print 'Module %s not added :(' % module['id']
            exit()
        elif os.path.exists(os.path.join(self.godotmodules_dir, module['dir'])):
            print 'Module %s already installed!' % module['id']
            exit()
        else:
            print 'Installing module %s...' % module['id'],
            Files.copy_anything(os.path.join(self.module_dir, module['dir']),
                                os.path.join(self.godotmodules_dir, module['dir']))
            if 'after-install' in module:
                self.actions.do_actions(module['after-install'])
            if 'after-install-firebase' in module and self.config.is_firebase():
                self.actions.do_actions(module['after-install-firebase'])
            print 'OK'

    def uninstall_module(self, module):
        """ Unistall module """
        if not os.path.exists(os.path.join(self.godotmodules_dir, module['dir'])):
            # Not installed
            return
        else:
            print 'Uninstalling module %s...' % module['id'],
            installed_folder = os.path.join(self.godotmodules_dir, module['dir'])
            Files.remove_folder(installed_folder)
            print 'OK'
