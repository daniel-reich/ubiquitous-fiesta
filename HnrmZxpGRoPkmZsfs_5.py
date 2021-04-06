
import datetime
def is_valid_date(d, m, y):
    try:
        datetime.datetime(int(y), int(m), int(d))
        return True
    except ValueError:
        return False

