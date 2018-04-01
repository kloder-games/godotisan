"""The module command."""

import os
import godotisan.utils.files as Files
from godotisan.libs.actions import Actions
from .base import Base

class Module(Base):
    """ Manage all modules commands """

    actions = None
    name = ''
    module_dir = ''

    def run(self):
        self.actions = Actions()
        self.name = self.options["<name>"]
        modules_dir = os.path.join(os.getcwd(), 'modules')

        if self.name == 'all':
            if self.options["add"]:
                print 'Not allowed all option for add action :('
                exit()
            else:
                for module in self.config.get_modules():
                    self.module_dir = os.path.join(modules_dir, module['id'])
                    self.action(module)
        elif self.options["list"]:
            self.list()
        else:
            module = self.library.get(self.name)
            self.module_dir = os.path.join(modules_dir, module['id'])
            if not self.options["add"]:
                module = self.config.get_module(self.name)
                self.module_dir = os.path.join(modules_dir, module['id'])
            self.action(module)


    def action(self, module):
        """ Select the action to perform """
        if self.options["add"]:
            self.add(module)
        elif self.options["remove"]:
            self.remove(module)

    def add(self, module):
        """ Add module to project """
        if not module:
            print 'Module %s not in library :(' % module['id']
            exit()
        print 'Adding module %s... ' % module['id'],
        modules_dir = os.path.join(os.getcwd(), 'modules')
        self.github.clone_module(modules_dir, module)
        self.config.add_module(module)
        print 'OK'

    def remove(self, module):
        """ Remove a module from project """
        if not module:
            print 'Module %s not found in config :(' % module['id']
        else:
            print 'Removing module %s...' % module['id'],
            Files.remove_folder(self.module_dir)
            self.config.remove_module(module)
            print 'OK'

    def list(self):
        """ List all modules in library """
        self.library.list()
