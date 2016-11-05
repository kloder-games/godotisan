"""
Scons Wrapper library
"""

import os, subprocess

class Scons():

    DEVNULL = open(os.devnull, 'wb')

    def __init__(self, cores = 4, stdout = DEVNULL):
        self.cores = cores
        self.stdout = stdout
        self.godotDir = os.path.join(os.getcwd(), 'godot')

    # Building

    def buildGodot(self):
        before = os.getcwd()
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=x11' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    def buildAndroidDebug(self):
        before = os.getcwd()
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=android target=release_debug tools=no android_arch=armv6 android_neon=no' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    def buildAndroidRelease(self):
        before = os.getcwd()
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=android target=release tools=no android_arch=armv6 android_neon=no' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    # Cleaning (Not used)

    def cleanGodot(self):
        before = os.getcwd()
        os.chdir(self.godotDir)
        subprocess.call('scons -c platform=android', shell=True, stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    def cleanAndroidDebug(self):
        before = os.getcwd()
        os.chdir(self.godotDir)
        subprocess.call('scons -c platform=android target=release_debug', shell=True, stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    def cleanAndroidRelease(self):
        before = os.getcwd()
        os.chdir(self.godotDir)
        subprocess.call('scons -c platform=android target=release', shell=True, stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)
