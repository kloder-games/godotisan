"""
Github Wrapper library
"""

import os
from git import Repo, Git

class Github():

    def __init__(self):
        pass

    # Clone

    def cloneModule(self, modulesDir, module):
        print 'Clonning %s repo...' % module['name']
        moduleDir = os.path.join(modulesDir, module['name'])
        Repo.clone_from(module['repo'], moduleDir)
        repo = Git(moduleDir)
        if 'tag' in module and module['tag'] != 'master':
            print 'Checkout to "%s" Tag...' % module['tag']
            repo.checkout(module['tag'])

    def cloneGodot(self, name):
        print 'Clonning Godot repo...'
        godotDir = os.path.join(name, 'godot')
        Repo.clone_from('git@github.com:godotengine/godot.git', godotDir)
        repo = Git(godotDir)
        print 'Checkout to "2.1-stable" Tag...'
        repo.checkout("2.1-stable")
