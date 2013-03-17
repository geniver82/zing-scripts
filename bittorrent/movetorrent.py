from base import foundation
import settings
from zingutils import fileutil
from zingutils import logutil

"""Folder paths to scan for torrent files from."""
SOURCE_DIRS = settings.SOURCE_DIRS

"""Folder path to move torrent files to."""
DESTINATION = settings.DESTINATION_DIR

"""File extensions to scan for."""
VALID_FILE_EXTENSIONS = settings.VALID_FILE_EXTENSIONS

def run():
    """Entry point"""
    'Perform bootstrap to filter out all the valid files to work with.'
    logutil.info('Running movetorrent')
    files = foundation.bootstrap(SOURCE_DIRS, VALID_FILE_EXTENSIONS)
            
    '''
    Move torrent files to destination folder to be picked up by Bittorrent
    client
    '''
    fileutil.move_files(DESTINATION, files)
