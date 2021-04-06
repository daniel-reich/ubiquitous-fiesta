
import datetime
def is_valid_date(d, m, y):
    x = True
    try :
        datetime.datetime(y,m,d)
    except ValueError:
        x=False
    return x

