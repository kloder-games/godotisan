"""Module helper command."""

from tempfile import mkstemp
from shutil import move, copytree, copy, rmtree, errno
from os import remove, close

def replace(file_path, pattern, subst):
    """ Replace a pattern in a file """
    #Create temp file
    fpo, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fpo)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def copy_anything(src, dst):
    """ Copy anything """
    try:
        copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            copy(src, dst)
        else: raise

def add_at_end(file_path, string):
    """ Add at end of file """
    if not file_has_string(file_path, string):
        with open(file_path, "a") as fpo:
            fpo.write(string)

def replace_file(file_path, subst):
    """ Replace file by other """
    remove(file_path)
    move(subst, file_path)

def remove_folder(folder):
    """ Remove folder """
    rmtree(folder)

def file_has_string(file_path, string):
    """ Check if a file has a string """
    if string in open(file_path).read():
        return True
    return False
