"""
Gradle Wrapper library
"""

import os, subprocess

class Gradle():

    DEVNULL = open(os.devnull, 'wb')

    def __init__(self, stdout = DEVNULL):
        self.stdout = stdout
        self.godotJavaDir = os.path.join(os.getcwd(), 'godot/platform/android/java/')

    # Building

    def build(self):
        before = os.getcwd()
        os.chdir(self.godotJavaDir)
        subprocess.call("./gradlew build", shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    # Cleaning

    def clean(self):
        before = os.getcwd()
        os.chdir(self.godotJavaDir)
        subprocess.call("./gradlew clean", shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)
