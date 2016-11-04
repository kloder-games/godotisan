"""Module helper command."""

from tempfile import mkstemp
from shutil import move, copytree, copy
from os import remove, close

def replace(file_path, pattern, subst):
    """
    Replace on file
    """
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                print line
                print line.replace(pattern, subst)
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def copyanything(src, dst):
    """
    Copy from a source to a destiny
    """
    try:
        copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            copy(src, dst)
        else: raise

def addatend(file_path, line):
    """
    Add line at the end of file
    """
    with open(file_path, "a") as f:
        f.write(line)

def replacefile(file_path, subst):
    """
    Replace file by other
    """
    remove(file_path)
    move(subst, file_path)
