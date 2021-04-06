
def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 28
    return 31
​
def day_of_year(date):
    month, day, year = [int(_) for _ in date.split('/')]
    if month == 1:
        return day
    return sum([days_in_month(m, year) for m in range(1, month)]) + day

