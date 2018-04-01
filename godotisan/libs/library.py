"""
Class for manage the modules configuration file
"""

import os
import json

class Library(object):
    """ Library Class """

    json = []

    def __init__(self):
        modules_dir = os.path.dirname(os.path.realpath(__file__))
        parent_modules_dir = os.path.join(modules_dir, os.pardir)
        if os.path.exists(modules_dir):
            with open(os.path.join(parent_modules_dir, 'modules.json')) as content:
                self.json = json.load(content)

    def has(self, module_id):
        """ Check module exists """
        if self.get(module_id):
            return True
        return False

    def get(self, module_id):
        """ Get module configuration """
        for module in self.json['modules']:
            if module['id'] == module_id:
                return module
        return None

    def list(self):
        """ List all modules avaiable """
        for module in self.json['modules']:
            print "%s (%s)" % (module['id'], module['tag'])

