import os
import sys

CURRENT_WORK_DIR = os.getcwd()
BASE_DIR = os.path.dirname(CURRENT_WORK_DIR)
sys.path.append(BASE_DIR)

'''Print PYTHON_PATH'''
#for path in sys.path:
#    print path

from zingutils import logutil
ORIGIN_FOLDER = os.path.join(CURRENT_WORK_DIR, 'origin')
DESTINATION_FOLDER = os.path.join(CURRENT_WORK_DIR, 'destination')
logutil.info('ORIGIN_FOLDER: %s' %(ORIGIN_FOLDER))
logutil.info('DESTINATION_FOLDER: %s' %(DESTINATION_FOLDER))


'''
Test scanning directories and identifying file extensions
'''
from base import foundation

print '### Running Test 1: Scanning for URL ###'
dirs_to_scan = [ORIGIN_FOLDER]
extensions = ['url']
files = foundation.bootstrap(dirs_to_scan, extensions)
for f in files:
    logutil.info('URL found: %s' %(f))

print '### Running Test 2: Scanning for Torrent ###'
extensions = ['torrent']    
files = foundation.bootstrap(dirs_to_scan, extensions)
for f in files:
    logutil.info('Torrent found: %s' %(f))
