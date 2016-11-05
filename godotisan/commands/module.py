"""The module command."""

import os
import utils.files as Files
from utils.actions import Actions
from .base import Base

class Module(Base):

    def run(self):
        self.actions = Actions()
        self.name = self.options["<name>"]
        modulesDir = os.path.join(os.getcwd(), 'modules')

        if self.name == 'all':
            if self.options["add"]: print 'Not allowed all option for add action :('; exit()
            else:
                for module in self.config.getModules():

                    self.moduleDir = os.path.join(modulesDir, module['name'])
                    self.action(module)
        else:
            module = self.library.getModule(self.name)
            self.moduleDir = os.path.join(modulesDir, module['name'])
            if not self.options["add"]:
                module = self.config.getModule(self.name)
                self.moduleDir = os.path.join(modulesDir, module['name'])
            self.action(module)


    def action(self, module):
        if self.options["add"]: self.add(module)
        elif self.options["install"]: self.install(module)
        elif self.options["reinstall"]: self.reinstall(module)
        elif self.options["uninstall"]: self.uninstall(module)
        elif self.options["remove"]: self.remove(module)

    def add(self, module):
        if not module:
            print 'Module %s not in library :(' % module['name']; exit()
        print 'Adding module %s... ' % module['name'],
        modulesDir = os.path.join(os.getcwd(), 'modules')
        self.github.cloneModule(modulesDir, module)
        self.config.addModule(module)
        print 'OK'

    def install(self, module):
        godotModulesDir = os.path.join(os.getcwd(), 'godot/modules')
        if not module:
            print 'Module %s not added :(' % module['name']; exit()
        elif os.path.exists(os.path.join(godotModulesDir, module['dir'])):
            print 'Module %s already installed!' % module['name']; exit()
        else:
            print 'Installing module %s...' % module['name'],
            Files.copyAnything(os.path.join(self.moduleDir, module['dir']), os.path.join(godotModulesDir, module['dir']))
            if 'after-install' in module: self.actions.doActions(module['after-install'])
            if 'after-install-firebase' in module and self.config.isFirebase(): self.actions.doActions(module['after-install-firebase'])
            print 'OK'

    def reinstall(self, module):
        self.uninstall(module)
        self.install(module)

    def uninstall(self, module):
        godotModulesDir = os.path.join(os.getcwd(), 'godot/modules')
        if not module:
            print 'Module %s not found in config :(' % module['name']
        elif not os.path.exists(os.path.join(godotModulesDir, module['dir'])):
            print 'Module %s not installed!' % module['name']
        else:
            print 'Uninstalling module %s...' % module['name'],
            installedFolder = os.path.join(godotModulesDir, module['dir'])
            Files.removeFolder(installedFolder)
            print 'OK'

    def remove(self, module):
        if not module:
            print 'Module %s not found in config :(' % module['name']
        else:
            print 'Removing module %s...' % module['name'],
            Files.removeFolder(self.moduleDir)
            self.config.removeModule(module)
            print 'OK'
