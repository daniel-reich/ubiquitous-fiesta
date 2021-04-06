
import datetime
def get_day(day):
    m, d, y = (int(i) for i in day.split('/'))
    return datetime.date(y, m, d).strftime("%A")

