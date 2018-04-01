"""
Management configuration
"""

import os
import json

class Config(object):
    """ Config tasks """

    data = {}

    def __init__(self):
        self.config_file = os.path.join(os.getcwd(), 'godotisan.json')
        if os.path.exists(self.config_file):
            with open(self.config_file) as content:
                self.data = json.load(content)

    def create(self, name):
        """ Create config file """
        data = self.read_from_template()
        self.config_file = os.path.join(name, 'godotisan.json')
        self.save(data)

    def read_from_template(self):
        """ Read from template """
        current_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(current_dir, os.pardir)
        file_path = os.path.join(template_dir, 'godotisan-template.json')
        with open(file_path) as data_file:
            data = json.load(data_file)
        return data

    def save(self, data):
        """ Save config """
        with open(self.config_file, 'w') as data_file:
            data_file.write(json.dumps(data, indent=4))

    def is_firebase(self):
        """ Check if firebase is active """
        if 'firebase' in self.data and self.data['firebase']:
            return True
        return False

    # Actions

    def get_actions(self, name):
        """ Get all actions """
        if name in self.data:
            return self.data[name]
        return None

    # Modules

    def get_modules(self):
        """ Get modules """
        if 'modules' in self.data:
            return self.data['modules']
        return {}

    def get_module(self, module_id):
        """ Get module """
        for module in self.data['modules']:
            if module['id'] == module_id:
                return module
        return None

    def has_module(self, module_id):
        """ Has module """
        return 'modules' in self.data and module_id in self.data['modules']

    def add_module(self, module):
        """ Add module """
        self.data['modules'].append(module)
        self.save(self.data)

    def remove_module(self, module):
        """ Remove module """
        self.data['modules'].remove(module)
        self.save(self.data)
