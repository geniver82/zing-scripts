import timeutil

__levelNames = {
    'DEBUG' : '[debug]',
    'WARN' : '[Warn]',
    'INFO' : '[Info]',
    'ERROR' : '[ERROR]',
    'FATAL' : '[WTF!!!]', # What a Terrible Failure
}

__empty_message = '[EMPTY MESSAGE]'


"""
A very simple log method.
"""
def __log__(level, message=__empty_message):
    '[Info] [%d-%m-%Y %H:%M:%S] message'
    err = '%s %s %s' %(level, timeutil.current_timestamp_str(), message)
    print err
    
def debug(message):
    __log__(__levelNames.get('DEBUG'), message)
    
def warn(message):
    __log__(__levelNames.get('WARN'), message)
    
def info(message):
    __log__(__levelNames.get('INFO'), message)
    
def error(message):
    __log__(__levelNames.get('ERROR'), message)
    
def fatal(message):
    __log__(__levelNames.get('FATAL'), message)
