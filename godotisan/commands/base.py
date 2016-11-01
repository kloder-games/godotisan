"""The base command."""

import os, json
import subprocess

class Base(object):
    """A base command."""

    currentDir = os.getcwd()
    godotDir = os.path.join(currentDir, 'godot')
    godotJavaDir = os.path.join(godotDir, 'platform/android/java')
    godotModulesDir = os.path.join(godotDir, 'modules')
    modulesDir = os.path.join(currentDir, 'modules')
    configFile = os.path.join(currentDir, 'godotisan.json')

    # For call output to null
    DEVNULL = open(os.devnull, 'wb')

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    # Manipulating the config file

    def saveConfigFile(self, data):
        with open(self.configFile, 'w') as outfile:
            outfile.write(json.dumps(data, indent=4, sort_keys=True))

    def readConfigFile(self):
        with open(os.path.join(self.configFile)) as outfile:
            return json.load(outfile)

    # Reading the modules files

    def readModulesFile(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(scriptDir, 'modules.json')) as outfile:
            return json.load(outfile)
