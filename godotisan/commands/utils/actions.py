"""
Actions class
"""

import os
import files as Files

class Actions():

    def __init__(self):
        pass

    def doActions(self, actions):
        for action in actions:
            self.doAction(action)

    def doAction(self, action):
        currentDir = os.getcwd()
        godotDir = os.path.join(currentDir, 'godot')
        if 'replace' in action:
            # Replace
            file_path = os.path.join(godotDir, action['file'])
            if not Files.fileHasString(file_path, action['replace'][1]):
                Files.replace(file_path, action['replace'][0],
                                action['replace'][1])
        elif 'add-line-after' in action:
            # Add Line After
            file_path = os.path.join(godotDir, action['file'])
            if not Files.fileHasString(file_path, action['add-line-after'][1]):
                Files.replace(file_path, action['add-line-after'][0],
                    action['add-line-after'][0] + '\n' + action['add-line-after'][1])
        elif 'add-line-at-end' in action:
            # Add Line At End
            file_path = os.path.join(godotDir, action['file'])
            if not Files.fileHasString(file_path, action['add-line-at-end']):
                Files.addAtEnd(file_path, action['add-line-at-end'])
        elif 'replace-by-file' in action:
            # Replace by File
            file_path = os.path.join(godotDir, action['file'])
            subst = os.path.join(godotDir, action['replace-by-file'])
            Files.replaceFile(file_path, subst)
        elif 'copy-file' in action:
            # Copy file
            file_path = os.path.join(currentDir, action['copy-file'])
            file_dir = os.path.join(godotDir, action['file'])
            Files.copyAnything(file_path, file_dir)
