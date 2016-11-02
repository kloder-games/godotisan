"""The create command."""

import os, json
from git import Repo, Git

from .base import Base

class Create(Base):
    """Create the Godot Build Project"""

    name = ""

    def run(self):
        self.name = self.options["<name>"]

        self.createDirectories()
        self.createConfigFile()
        self.cloneGodot()

        print 'Project %s created!' % self.name
        print 'Build something awesome!'

    def createDirectories(self):
        if not os.path.exists(self.name):
            os.makedirs(self.name)
        else:
            print 'The project already exists :('
            exit()

        os.makedirs(os.path.join(self.name, 'godot'))
        os.makedirs(os.path.join(self.name, 'modules'))

    def createConfigFile(self):
        config = '{ "tag": "2.1-stable", "firebase": false, "modules": [] }'

        self.configFile = os.path.join(self.name, 'godotisan.json')
        with open(self.configFile, 'w') as outfile:
            outfile.write(json.dumps(json.loads(config), indent=4, sort_keys=True))

    def cloneGodot(self):
        print 'Clonning Godot repo...'
        godotDir = os.path.join(self.name, 'godot')
        Repo.clone_from('git@github.com:godotengine/godot.git', godotDir)
        repo = Git(godotDir)
        print 'Checkout to "2.1-stable" Tag...'
        repo.checkout("2.1-stable")
