
import datetime
​
def months_interval(start, end) -> list:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    if start > end:
        temp = start
        start = end
        end = temp
​
    if start == end:
        return [months[start.month - 1]]
    elif end.year - start.year > 1 or end.month - start.month == 12 or \
            (end.year - start.year == 1 and end.month - start.month >= -1):
        return months
    elif end.year == start.year:
        return months[start.month - 1: end.month]
    else:
        return months[: end.month] + months[start.month - 1:]

