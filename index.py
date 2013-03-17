import os
import settings
import sys
from time import sleep

MODULES = settings.MODULES_INSTALLED

SLEEP_DURATION_IN_SECS = settings.SLEEP_DURATION_IN_MINS * 60

__valid_modules__ = []

def run():
    __prerun__()
    while(True):
        __run_modules__()

        from zingutils import logutil
        logutil.info('Sleeping for %s minutes.' 
            %(str(settings.SLEEP_DURATION_IN_MINS)))
        sleep(SLEEP_DURATION_IN_SECS)

def __prerun__():
    __add_libraries_to_python_path__()
    __import_libraries__()    

def __add_libraries_to_python_path__():
    current_work_dir = os.getcwd()
    sys.path.append(current_work_dir)

def __import_libraries__():
    for module in MODULES:
        module_entity = __import__(module, fromlist='*')
        __valid_modules__.append(module_entity)

def __run_modules__():
    for module in __valid_modules__:
        module.run()

run()