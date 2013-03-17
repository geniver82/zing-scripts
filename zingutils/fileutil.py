import logutil
import os
import shutil

def delete_file(f):
    """Delete single file from filesystem"""
    if f != None:    
        logutil.info('Removing %s' %(f))
        os.unlink(f)

def delete_files(files=[]):
    """Delete multiple files from filesystem"""    
    for f in files:
        delete_file(f)    

def filter_files(files=[], extensions=[]):
    """Return a list of files that only match the given extension."""
    valid_files = []
    for f in files:
        'Check if f extension is valid'
        is_valid_file = is_valid_file_extension(f, extensions)

        'Add to list if f is valid'
        if(is_valid_file):
            valid_files.append(f)
        else:
            logutil.info('File skipped: ' + f)
    return valid_files

def is_valid_file_extension(filename, extensions):
    """Return if file is a valid file extension to read."""
    for ext in extensions:
        if filename.endswith(ext):
            return True

def list_files(dirs=[]):
    """
    1. Read a list of directories
    2. Append respective directory path to every files in the list.
    3. Return this list of files.
    """
    all_files = []
    for d in dirs:
        'return a list of all files in directory'
        files = os.listdir(d)
    
        'append directory path to every file in list'
        for f in files:
            full_path = os.path.join(d, f) 
            all_files.append(full_path)

    'return this list of files'
    return all_files

def move_file(destination, f):
    logutil.info('Moving %s to %s' %(f, destination))
    shutil.move(f, destination)

def move_files(destination, files=[]):
    for f in files:
        move_file(f, destination)

def read_file(filename=None):
    """Read the txt file and return the contents as a list."""
    contents = []
    try:
        f = open(filename)
        contents = f.readlines()
    except IOError:
        print IOError        
    return contents



