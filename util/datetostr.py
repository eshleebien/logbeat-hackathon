import datetime
import time

def datestr_to_unix(date_str):
    return int(time.mktime(datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").timetuple()))
