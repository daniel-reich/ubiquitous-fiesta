
import datetime
​
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
​
def months_interval(dateStart, dateEnd):
    year1 = dateStart.year
    month1 = dateStart.month - 1
    year2 = dateEnd.year
    month2 = dateEnd.month - 1
    if (year1, month1) > (year2, month2):
        year1, month1, year2, month2 = year2, month2, year1, month1
    if year2 - year1 > 1:
        return MONTHS
    if year1 == year2 and month1 == month2:
        return [MONTHS[month1]]
    if year2 == year1:
        return MONTHS[month1:month2+1]
    if year2 == year1 + 1:
        months = set()
        months.add(MONTHS[month1])
        while (year1 != year2) or (month1 != month2):
            month1 += 1
            if month1 == 12:
                year1 += 1
                month1 = 0
            months.add(MONTHS[month1])
        months = [[m, MONTHS.index(m)] for m in months]
        months.sort(key=lambda x: x[1])
        return [m[0] for m in months]

