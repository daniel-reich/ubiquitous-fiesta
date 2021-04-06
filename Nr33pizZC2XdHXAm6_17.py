
import datetime
​
​
def months_interval(date_start, date_end):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    if date_start > date_end:
        date_start, date_end = date_end, date_start
    if date_start.year == date_end.year:
        return months[date_start.month - 1: date_end.month]
    elif date_end.year - date_start.year > 1:
        return months
    else:
        if date_end.month < date_start.month:
            return months[:date_end.month] + months[date_start.month - 1:]
        else:
            return months

