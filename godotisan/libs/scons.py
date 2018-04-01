"""
Scons Wrapper library
"""

import os
import subprocess

class Scons(object):
    """ Scons Class """

    DEVNULL = open(os.devnull, 'wb')

    def __init__(self, cores=4, stdout=DEVNULL):
        self.cores = cores
        self.stdout = stdout
        self.godot_dir = os.path.join(os.getcwd(), 'godot')

    # Building

    def build_godot(self):
        """ Build Godot """
        before = os.getcwd()
        os.chdir(self.godot_dir)
        subprocess.call('scons -j%d platform=x11' % self.cores, shell=True, stdout=self.stdout,
                        close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    def build_android_debug(self):
        """ Build Android Debug """
        before = os.getcwd()
        os.chdir(self.godot_dir)
        subprocess.call('scons -j%d platform=android target=release_debug' % self.cores,
                        shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)
        #  android_arch=armv6 android_neon=no

    def build_android_release(self):
        """ Build Android Release """
        before = os.getcwd()
        os.chdir(self.godot_dir)
        subprocess.call('scons -j%d platform=android target=release' % self.cores,
                        shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)
        # android_arch=armv6 android_neon=no

    # Cleaning (Not used)

    def clean_godot(self):
        """ Clean Godot """
        before = os.getcwd()
        os.chdir(self.godot_dir)
        subprocess.call('scons -c platform=android', shell=True, stdout=self.DEVNULL,
                        close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    def clean_android_debug(self):
        """ Clean Android Debug """
        before = os.getcwd()
        os.chdir(self.godot_dir)
        subprocess.call('scons -c platform=android target=release_debug', shell=True,
                        stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)

    def clean_android_release(self):
        """ Clean Android Release """
        before = os.getcwd()
        os.chdir(self.godot_dir)
        subprocess.call('scons -c platform=android target=release', shell=True, stdout=self.DEVNULL,
                        close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(before)
