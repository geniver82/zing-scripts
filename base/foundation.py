from zingutils import fileutil
from zingutils import logutil

def bootstrap(dirs_to_scan=[], extensions_to_scan=[]):
    '''
    Perform all boilerplate processes such as scanning folders for files and
    returning only those that matches the required file extensions. 
    '''
    files = fileutil.list_files(dirs_to_scan)

    valid_files = []
    'if there are no files in directory'
    if len(files) == 0:
        logutil.info('No files found.')
    else:
        'Extract all valid files for scanning'
        valid_files = fileutil.filter_files(files, extensions_to_scan)
    
    return valid_files        

