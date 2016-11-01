"""The check command."""


import os
import subprocess

from .base import Base


class Build(Base):
    """Check requirements"""

    def run(self):
        self.checkScons()
        self.checkJava()
        self.checkGradle()

    def checkScons(self):
        print 'Checking sconds... ',
        try:
            p = subprocess.Popen(['scons', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            print 'OK'
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print 'Not found'
            else:
                print 'Error'

    def checkGradle(self):
        print 'Checking gradle... ',
        try:
            p = subprocess.Popen(['gradle', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            print 'OK'
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print 'Not found'
            else:
                print 'Error'


    def checkJava(self):
        print 'Checking java... ',
        try:
            p = subprocess.Popen(['java', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            print 'OK'
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print 'Not found'
            else:
                print 'Error'
