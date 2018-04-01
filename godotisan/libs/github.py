"""
Github Wrapper library
"""

import os
from git import Repo, Git

class Github(object):
    """ Github Class """

    def __init__(self):
        pass

    # Clone

    def clone_module(self, modules_dir, module):
        """ Clone a module """
        module_dir = os.path.join(modules_dir, module['id'])
        Repo.clone_from(module['repo'], module_dir)
        repo = Git(module_dir)
        if 'tag' in module and module['tag'] != 'master':
            repo.checkout(module['tag'])

    def clone_godot(self, name):
        """ Clone Godot """
        print 'Clonning Godot repo...'
        godot_dir = os.path.join(name, 'godot')
        Repo.clone_from('git@github.com:godotengine/godot.git', godot_dir)
        repo = Git(godot_dir)
        print 'Checkout to "2.1-stable" Tag...'
        repo.checkout("2.1-stable")
