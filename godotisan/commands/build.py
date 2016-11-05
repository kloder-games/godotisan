"""The build command."""

import os

from utils.scons import Scons
from utils.gradle import Gradle
from utils.actions import Actions

import utils.files as Files

from .base import Base

class Build(Base):
    """Build the Godot project"""

    DEVNULL = open(os.devnull, 'wb')

    def run(self):
        cores = 0
        stdout = None

        if self.options['--cores']: cores = int(self.options['--cores'])
        if not self.options['--debug']: stdout = self.DEVNULL

        actions = Actions()
        scons = Scons(cores, stdout)
        gradle = Gradle(stdout)

        if self.options['godot']:
            scons.buildGodot()
            print 'Godot build successfuly!'

        elif self.options['android']:
            print 'Processing before build rules... ',
            if self.config.getActions('before-build') != None: actions.doActions(self.config.getActions('before-build'))
            if self.config.isFirebase() and self.config.getActions('before-build-firebase') != None: actions.doActions(self.config.getActions('before-build-firebase'))
            print 'OK'

            print 'Cleaning builds... ',
            gradle.clean()
            print 'OK'

            if self.options['--only-debug']:
                print 'Building debug template... ',
                scons.buildAndroidDebug()
            elif self.options['--only-release']:
                print 'Building release template... ',
                scons.buildAndroidRelease()
            else:
                print 'Building release & debug template... ',
                scons.buildAndroidRelease()
                gradle.build()
                gradle.clean()
                scons.buildAndroidDebug()
            gradle.build()
            print 'OK'
