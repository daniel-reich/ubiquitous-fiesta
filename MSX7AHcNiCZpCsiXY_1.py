
import calendar
​
def how_unlucky(y):
    return sum(calendar.weekday(y, m, 13) == 4 for m in range(1, 13))

