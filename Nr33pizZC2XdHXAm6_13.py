
import datetime
​
​
def months_interval(dateStart, dateEnd):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
​
    if dateStart > dateEnd: dateStart, dateEnd = dateEnd, dateStart
​
    month_start = int(dateStart.strftime('%m'))
    month_end = int(dateEnd.strftime('%m'))
    year_start = int(dateStart.strftime('%y'))
    year_end = int(dateEnd.strftime('%y'))
​
    year_diff = year_end - year_start
​
    iter_month = (month_end - month_start) + year_diff * 12
​
    lst = []
    for m_i in range(month_end - 1 - iter_month, month_end):
        lst.append(months[m_i % 12])
​
    return list(sorted(set(lst), key=months.index))

