"""
Actions class
"""

import os
import godotisan.utils.files as Files

class Actions(object):
    """ Actions tasks """

    def __init__(self):
        pass

    def do_actions(self, actions):
        """ Do all actions """
        for action in actions:
            self.do_action(action)

    def do_action(self, action):
        """ Execute action """
        current_dir = os.getcwd()
        godot_dir = os.path.join(current_dir, 'godot')
        if 'replace' in action:
            # Replace
            file_path = os.path.join(godot_dir, action['file'])
            if not Files.file_has_string(file_path, action['replace'][1]):
                Files.replace(file_path, action['replace'][0], action['replace'][1])
        elif 'add-line-after' in action:
            # Add Line After
            file_path = os.path.join(godot_dir, action['file'])
            if not Files.file_has_string(file_path, action['add-line-after'][1]):
                Files.replace(file_path, action['add-line-after'][0], action['add-line-after'][0] +
                              '\n' + action['add-line-after'][1])
        elif 'add-line-at-end' in action:
            # Add Line At End
            file_path = os.path.join(godot_dir, action['file'])
            if not Files.file_has_string(file_path, action['add-line-at-end']):
                Files.add_at_end(file_path, action['add-line-at-end'])
        elif 'replace-by-file' in action:
            # Replace by File
            file_path = os.path.join(godot_dir, action['file'])
            subst = os.path.join(godot_dir, action['replace-by-file'])
            Files.replace_file(file_path, subst)
        elif 'copy-file' in action:
            # Copy file
            file_path = os.path.join(current_dir, action['copy-file'])
            file_dir = os.path.join(godot_dir, action['file'])
            Files.copy_anything(file_path, file_dir)
