"""The base command."""

from godotisan.libs.config import Config
from godotisan.libs.library import Library
from godotisan.libs.github import Github

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
        """ Default run behaviour """
        raise NotImplementedError('You must implement the run() method yourself!')
