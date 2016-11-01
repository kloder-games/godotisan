"""The build command."""

import os, subprocess

from .base import Base

class Build(Base):
    """Build the Godot project"""

    cores = 0
    stdout = None

    def run(self):
        if self.options['--cores']: self.cores = int(self.options['--cores'])
        if not self.options['--debug']: self.stdout = self.DEVNULL

        if self.options['godot']:
            self.compileGodot(cores)
            print 'Godot build successfuly!'

        elif self.options['android']:
            if self.options['--only-debug']:
                self.compileAndroidTemplateDebug()
            elif self.options['--only-release']:
                self.compileAndroidTemplateRelease()
            else:
                self.compileAndroidTemplateRelease()
                self.compileAndroidTemplateDebug()
            print 'Templates build successfuly!'

    def compileGodot(self):
        print 'Compiling Godot with %d cores...' % self.cores
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=x11' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)

    def compileAndroidTemplateRelease(self):
        self.cleanBuild()
        print 'Compiling android template release with %d cores...' % self.cores
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=android target=release' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        print 'Gradle android template release ...'
        os.chdir(self.godotJavaDir)
        subprocess.call("./gradlew build", shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)

    def compileAndroidTemplateDebug(self):
        self.cleanBuild()
        print 'Compiling android template debug with %d cores...' % self.cores
        os.chdir(self.godotDir)
        subprocess.call('scons -j%d platform=android target=release_debug' % self.cores, shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
        print 'Gradle android template debug ...'
        os.chdir(self.godotJavaDir)
        subprocess.call("./gradlew build", shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)


    # Clean the builds with scons

    def cleanBuild(self):
        print 'Cleaning before compile...'
        # os.chdir(self.godotDir)
        # subprocess.call('scons -c platform=android', shell=True, stdout=self.DEVNULL, close_fds=True, stderr=subprocess.STDOUT)
        os.chdir(self.godotJavaDir)
        subprocess.call("./gradlew clean", shell=True, stdout=self.stdout, close_fds=True, stderr=subprocess.STDOUT)
