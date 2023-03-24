import datetime
import pytz

def parse_date_string(date_string, format='%Y-%m-%d'):
    return datetime.datetime.strptime(date_string, format)

def format_date_string(date_obj, format='%Y-%m-%d'):
    return date_obj.strftime(format)

def calculate_time_difference(start_time, end_time):
    time_diff = end_time - start_time
    return time_diff.total_seconds()

def convert_to_utc(date_obj, timezone='US/Eastern'):
    tz = pytz.timezone(timezone)
    local_time = tz.localize(date_obj)
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time