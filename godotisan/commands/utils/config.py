"""
Management configuration
"""

import os, json

class Config():

    data = {}

    def __init__(self):
        self.configFile = os.path.join(os.getcwd(), 'godotisan.json')
        if os.path.exists(self.configFile):
            with open(self.configFile) as f:
                self.data = json.load(f)

    def create(self, name):
        data = self.readFromTemplate()
        self.configFile = os.path.join(name, 'godotisan.json')
        self.save(data)

    def readFromTemplate(self):
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'godotisan-template.json')
        with open(file_path) as f:
            return json.loads(f)

    def save(self, data):
        with open(self.configFile, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=4))

    def isFirebase(self):
        if 'firebase' in self.data and self.data['firebase']: return True
        return False

    # Actions

    def getActions(self, name):
        if name in self.data: return self.data[name]
        return None

    # Modules

    def getModules(self):
        if 'modules' in self.data: return self.data['modules']
        return {}

    def getModule(self, moduleName):
        for module in self.data['modules']:
            if module['name'] == moduleName: return module
        return None

    def hasModule(self, moduleName):
        if 'modules' in self.data and moduleName in self.data['modules']: return True
        return False

    def addModule(self, module):
        self.data['modules'].append(module)
        self.save(self.data)

    def removeModule(self, module):
        self.data['modules'].remove(module)
        self.save(self.data)
