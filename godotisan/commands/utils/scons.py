"""
Scons Wrapper library
"""

import os, subprocess

class Scons():

    DEVNULL = open(os.devnull, 'wb')

    def __init__(self, godotDir, cores = 4, stdout = DEVNULL):
        self.cores = cores
        self.stdout = stdout
        self.godotDir = godotDir

    # Building

    def buildGodot(self):
        print 'Compiling Godot with %d cores...' % self.cores
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=x11' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)

    def buildAndroidDebug(self):
        print 'Compiling android template debug with %d cores...' % self.cores
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=android target=release_debug tools=no android_arch=armv6 android_neon=no' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)

    def buildAndroidRelease(self):
        print 'Compiling android template release with %d cores...' % self.cores
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=android target=release tools=no android_arch=armv6 android_neon=no' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)

    # Cleaning (Not used)

    def cleanGodot(self):
        print 'Cleaning scons godot before compile...'
        os.chdir(self.godotDir)
        subprocess.call('scons -c platform=android', shell=True, stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)

    def cleanAndroidDebug(self):
        print 'Cleaning scons android debug before compile...'
        os.chdir(self.godotDir)
        subprocess.call('scons -c platform=android target=release_debug', shell=True, stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)

    def cleanAndroidRelease(self):
        print 'Cleaning scons android release before compile...'
        os.chdir(self.godotDir)
        subprocess.call('scons -c platform=android target=release', shell=True, stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)
