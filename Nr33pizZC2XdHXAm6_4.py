
import datetime
​
def months_interval(dateStart, dateEnd):
    if dateStart > dateEnd:
        tempDate = dateStart
        dateStart = dateEnd
        dateEnd = tempDate
    arr = []
    mnths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    M = (dateEnd.month - dateStart.month)
    M2 = (dateEnd.year - dateStart.year) * 12
    numMonths = (M + M2) + 1
    for x in range(numMonths):
        if x + dateStart.month > 12:
            a = ((x + dateStart.month) % 12) - 1
        else:
            a = (x + dateStart.month) - 1
        arr.append(mnths[a])
    a = sorted(list(set(arr)), key = mnths.index)
    return a

