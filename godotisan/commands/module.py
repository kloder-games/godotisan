"""The module command."""

import os, json, shutil, errno
from subprocess import call
from git import Repo, Git
import utils.files as Files

from .base import Base

class Module(Base):
    """Manage modules"""

    config = []
    modules = []
    name = ""
    moduleDir = ""
    moduleFromModules = {}
    moduleFromConfig = {}

    def run(self):

        self.modules = self.readModulesFile()
        self.config = self.readConfigFile()
        self.name = self.options["<name>"]

        self.moduleFromModules = self.getModuleFromModules()
        self.moduleFromConfig = self.getModuleFromConfig()
        self.moduleDir = os.path.join(self.modulesDir, self.name)

        if self.options["add"]:
            self.add()
        elif self.options["install"]:
            self.install()
        elif self.options["uninstall"]:
            self.uninstall()
        elif self.options["remove"]:
            self.remove()

    def add(self):
        if self.moduleFromModules == None:
            print 'Module not found :('
        elif self.moduleFromConfig != None:
            print 'Module already added!'
        elif os.path.exists(self.moduleDir):
            self.config['modules'].append(self.module)
            self.saveConfigFile(self.config)
            print 'Module already added! (fixed godotisan.json)'
        else:
            print 'Clonning %s repo...' % self.name
            Repo.clone_from(self.moduleFromModules['repo'], self.moduleDir)
            repo = Git(self.moduleDir)
            if 'tag' in self.moduleFromModules and self.moduleFromModules['tag'] != 'master':
                print 'Checkout to "%s" Tag...' % self.moduleFromModules['tag']
                repo.checkout(self.moduleFromModules['tag'])

            self.config['modules'].append(self.moduleFromModules)
            self.saveConfigFile(self.config)
            print 'Module %s installed successfuly!' % self.name

    def install(self):
        if self.moduleFromConfig == None:
            print 'Module not found :('
        elif not os.path.exists(self.moduleDir):
            print 'Module not added :('
        elif os.path.exists(os.path.join(self.godotModulesDir, self.moduleFromConfig['dir'])):
            print 'Module already installed!'
        else:
            print 'Installing module %s...' % self.name
            Files.copyanything(os.path.join(self.moduleDir, self.moduleFromConfig['dir']),
                        os.path.join(self.godotModulesDir, self.moduleFromConfig['dir']))

            # Before compile actions
            if 'after_install' in self.moduleFromConfig:
                # After Install
                for action in self.moduleFromConfig['after_install']:
                    if 'replace' in action:
                        # Replace
                        file_path = os.path.join(self.godotDir, action['file'])
                        Files.replace(file_path, action['replace'][0],
                                        action['replace'][1])
                    elif 'add-line-after' in action:
                        # Add Line After
                        file_path = os.path.join(self.godotDir, action['file'])
                        Files.replace(file_path, action['add-line-after'][0],
                            action['add-line-after'][0] + '\n' + action['add-line-after'][1])
                    elif 'add-line-at-end' in action:
                        # Add Line At End
                        file_path = os.path.join(self.godotDir, action['file'])
                        Files.addatend(file_path, action['add-line-at-end'])
            if 'after-install-firebase' in self.moduleFromConfig:
                # After install if has firebase
                config = self.readConfigFile()
                if config['firebase']:
                    if 'replace-by-file' in action:
                        # Replace by File
                        file_path = os.path.join(self.godotDir, action['file'])
                        subst = os.path.join(self.godotDir, action['replace-by-file'])
                        Files.replacefile(file_path, subst)

            print 'Module %s installed successfully!' % self.name

    def uninstall(self):
        if self.moduleFromConfig == None:
            print 'Module not found :('
        elif not os.path.exists(os.path.join(self.godotModulesDir, self.moduleFromConfig['dir'])):
            print 'Module not installed!'
        else:
            print 'Uninstalling module %s...' % self.name
            installedFolder = os.path.join(self.godotModulesDir, self.moduleFromConfig['dir'])
            shutil.rmtree(installedFolder)
            print 'Module %s unisntalled successfully!' % self.name

    def remove(self):
        if self.moduleFromConfig == None:
            print 'Module not found :('
        elif not os.path.exists(self.moduleDir):
            self.config['modules'].remove(self.moduleFromConfig)
            self.saveConfigFile(self.config)
            print 'Module not added! (fixed godotisan.json)'
        else:
            print 'Removing module %s...' % self.name
            shutil.rmtree(self.moduleDir)
            self.config['modules'].remove(self.moduleFromConfig)
            self.saveConfigFile(self.config)
            print 'Module %s removed successfully!' % self.name

    # Utilities

    def getModuleFromConfig(self):
        for module in self.config['modules']:
            if module['name'] == self.name:
                return module
        return None

    def getModuleFromModules(self):
        for module in self.modules['modules']:
            if module['name'] == self.name:
                return module
        return None
