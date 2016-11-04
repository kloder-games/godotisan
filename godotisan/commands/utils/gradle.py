"""
Gradle Wrapper library
"""

import os, subprocess

class Gradle():

    DEVNULL = open(os.devnull, 'wb')

    def __init__(self, godotJavaDir, stdout = DEVNULL):
        self.stdout = stdout
        self.godotJavaDir = godotJavaDir

    # Building

    def build(self):
        print 'Gradle android template ...'
        os.chdir(self.godotJavaDir)
        subprocess.call("./gradlew build", shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)

    # Cleaning

    def clean(self):
        print 'Cleaning before compile...'
        os.chdir(self.godotJavaDir)
        subprocess.call("./gradlew clean", shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
