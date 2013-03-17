from datetime import datetime

"""
Convert minutes to seconds
"""
def convert_min_to_sec(minutes=0):
    return 1*60*minutes

"""
Get current date time in string
"""
def current_timestamp_str():
    today = datetime.today()
    date_string = today.strftime('[%d-%m-%Y %H:%M:%S]')
    return date_string