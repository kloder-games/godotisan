"""
Class for manage the modules configuration file
"""

import os, json

class Library():

    json = []

    def __init__(self):
        modulesDir = os.path.dirname(os.path.realpath(__file__))
        if os.path.exists(modulesDir):
            with open(os.path.join(modulesDir, 'modules.json')) as f:
                self.json = json.load(f)

    def has(self, moduleName):
        if self.get(moduleName): return True
        return False

    def get(self, moduleName):
        for module in self.json['modules']:
            if module['name'] == moduleName:
                return module
        return None
