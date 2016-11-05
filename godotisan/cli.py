#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
godotisan.py

Usage:
  godotisan check
  godotisan create <name>
  godotisan build godot [--cores=<nc>] [--debug]
  godotisan build android [--cores=<nc>] [--only-debug | --only-release] [--debug]
  godotisan module add <name>
  godotisan module install <name>
  godotisan module reinstall <name>
  godotisan module uninstall <name>
  godotisan module remove <name>
  godotisan -h | --help
  godotisan --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  --cores=<nc>                      Build with this number of cores
  --only-debug                      Build only for debug
  --only-release                    Build only for release
  --debug                           Show debug output for each command

Examples:
  godotisan create my_project

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/jlopezcur/godotisan
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.iteritems():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base' and command[0] != 'Git' and command[0] != 'Actions'][0]
            command = command(options)
            command.run()
