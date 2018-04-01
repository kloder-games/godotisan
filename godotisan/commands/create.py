"""The create command."""

import os
from .base import Base

class Create(Base):
    """Create the Godot Build Project"""

    def run(self):
        name = self.options["<name>"]

        self.create_directories(name)
        self.config.create(name)
        self.github.clone_godot(name)

        print 'Project %s created!' % name
        print 'Build something awesome!'

    def create_directories(self, name):
        """ Create the required directories """
        if not os.path.exists(name):
            os.makedirs(name)
        else:
            print 'The project already exists :('
            exit()

        os.makedirs(os.path.join(name, 'godot'))
        os.makedirs(os.path.join(name, 'modules'))
