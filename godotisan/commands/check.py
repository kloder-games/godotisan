"""The check command."""


import os
import subprocess

from .base import Base


class Build(Base):
    """Check requirements"""

    def run(self):
        self.check_scons()
        self.check_java()
        self.check_gradle()

    def check_scons(self):
        """ Check the Scons enviroment """
        print 'Checking Scons... ',
        try:
            proc = subprocess.Popen(['scons', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()
            print err
            print 'OK'
        except OSError as err:
            if err.errno == os.errno.ENOENT:
                print 'Not found'
            else:
                print 'Error'

    def check_gradle(self):
        """ Check the Gradle enviroment """
        print 'Checking gradle... ',
        try:
            proc = subprocess.Popen(['gradle', '-v'], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            out, err = proc.communicate()
            print err
            print 'OK'
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print 'Not found'
            else:
                print 'Error'


    def check_java(self):
        """ Check the Java enviroment """
        print 'Checking java... ',
        try:
            proc = subprocess.Popen(['java', '-version'], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            out, err = proc.communicate()
            print err
            print 'OK'
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print 'Not found'
            else:
                print 'Error'
