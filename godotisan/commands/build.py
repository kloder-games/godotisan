"""The build command."""

import os, subprocess

from utils.scons import Scons
from utils.gradle import Gradle
import utils.files as Files
from .base import Base

class Build(Base):
    """Build the Godot project"""

    scons = None
    gradle = None
    godotJavaDir = ""

    def run(self):
        cores = 0
        stdout = None
        self.godotJavaDir = os.path.join(self.godotDir, 'platform/android/java')

        if self.options['--cores']: cores = int(self.options['--cores'])
        if not self.options['--debug']: stdout = self.DEVNULL

        scons = Scons(self.godotDir, cores, stdout)
        gradle = Gradle(self.godotJavaDir, stdout)

        if self.options['godot']:
            scons.buildGodot()
            print 'Godot build successfuly!'

        elif self.options['android']:
            config = self.readConfigFile()
            if config['firebase']: self.firebaseCopy()

            gradle.clean()
            if self.options['--only-debug']:
                scons.buildAndroidDebug()
                print 'Template build successfuly!'
            elif self.options['--only-release']:
                scons.buildAndroidRelease()
                print 'Template build successfuly!'
            else:
                scons.buildAndroidRelease()
                gradle.build()
                gradle.clean()
                scons.buildAndroidDebug()
                print 'Templates build successfuly!'
            gradle.build()

    def firebaseCopy(self):
        print 'Copying file android-service.json to project... ',
        firebaseFile = os.path.join(self.currentDir, 'google-services.json')
        Files.copyanything(firebaseFile, self.godotJavaDir)
        print 'OK'
