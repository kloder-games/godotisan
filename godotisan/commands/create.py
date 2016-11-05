"""The create command."""

import os
from .base import Base

class Create(Base):
    """Create the Godot Build Project"""

    def run(self):
        self.name = self.options["<name>"]

        self.createDirectories()
        self.config.create(self.name)
        self.github.cloneGodot(self.name)

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
