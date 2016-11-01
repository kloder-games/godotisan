"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from godotisan import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=godtisan', '--cov-report=term-missing'])
        raise SystemExit(errno)

setup(
    name = 'godotisan',
    version = __version__,
    description = 'A command line interface for templates compilation and modules management.',
    long_description = long_description,
    url = 'https://github.com/jlopezcur/godotisan',
    author = 'Javier López Úbeda',
    author_email = 'jlopezcur@gmail.com',
    license = 'MIT',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: MIT',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'godotisan',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'gitpython'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'godotisan=godotisan.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
