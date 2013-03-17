from base import foundation
import settings
import webbrowser
from zingutils import fileutil
from zingutils import logutil

"""Root directories."""
ROOT_DIRS = settings.ROOT_DIRS

"""File extensions to scan for."""
VALID_FILE_EXTENSIONS = settings.VALID_FILE_EXTENSIONS

def run():
    """Entry point"""
    'Perform bootstrap to filter out all the valid files to work with.'
    logutil.info('Running urltobrowser')
    files = foundation.bootstrap(ROOT_DIRS, VALID_FILE_EXTENSIONS)    

    'Extract all urls from the files'
    urls = __extract_url__(files)

    'Housekeep files'
    fileutil.delete_files(files)

    'Open all urls in browser as new tab'
    __open_in_browser__(urls)
        
def __extract_url__(filenames=[]):
    """Extract all urls from files."""
    urls = []
    for filename in filenames:
        'Read file.'
        contents = fileutil.read_file(filename)    

        'Append URLs to list.'    
        for content in contents:
            urls.append(content)
    return urls    

def __open_in_browser__(urls=[]):
    """Open urls in browser's new tab."""
    for url in urls:
        logutil.info('Opening %s' %(url))
        webbrowser.open(url, new=1)
