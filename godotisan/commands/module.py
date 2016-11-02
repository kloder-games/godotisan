"""The module command."""

import os, json, shutil, errno
from subprocess import call
from git import Repo, Git

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
            self.copyanything(os.path.join(self.moduleDir, self.moduleFromConfig['dir']),
                        os.path.join(self.godotModulesDir, self.moduleFromConfig['dir']))
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
