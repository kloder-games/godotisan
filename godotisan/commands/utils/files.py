"""Module helper command."""

from tempfile import mkstemp
from shutil import move, copytree, copy, rmtree, errno
from os import remove, close

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def copyAnything(src, dst):
    try:
        copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            copy(src, dst)
        else: raise

def addAtEnd(file_path, string):
    if not fileHasString(file_path, string):
        with open(file_path, "a") as f:
            f.write(string)

def replaceFile(file_path, subst):
    """
    Replace file by other
    """
    remove(file_path)
    move(subst, file_path)

def removeFolder(folder):
    rmtree(folder)

def fileHasString(file_path, string):
    if string in open(file_path).read():
        return True
    return False
