"""
Gradle Wrapper library
"""

import os
import subprocess

class Gradle(object):
    """ Gradle Class """

    DEVNULL = open(os.devnull, 'wb')

    def __init__(self, stdout=DEVNULL):
        self.stdout = stdout
        self.godot_java_dir = os.path.join(os.getcwd(), 'godot/platform/android/java/')

    # Building

    def build(self):
        """ Build Gradle """
        before = os.getcwd()
        os.chdir(self.godot_java_dir)
        subprocess.call("./gradlew build", shell=True, stdout=self.stdout, close_fds=True,
                        stderr=subprocess.STDOUT)
        os.chdir(before)

    # Cleaning

    def clean(self):
        """ Clean Gradle """
        before = os.getcwd()
        os.chdir(self.godot_java_dir)
        subprocess.call("./gradlew clean", shell=True, stdout=self.stdout, close_fds=True,
                        stderr=subprocess.STDOUT)
        os.chdir(before)
