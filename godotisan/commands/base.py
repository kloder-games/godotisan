"""The base command."""

import os, json
from utils.config import Config
from utils.library import Library
from utils.github import Github

class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.config = Config()
        self.library = Library()
        self.github = Github()

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')
