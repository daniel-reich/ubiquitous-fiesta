
from datetime import date
def time_for_milk_and_cookies(date):
    dt = date
    if dt.strftime("%m") == '12':
        return True
    return False

