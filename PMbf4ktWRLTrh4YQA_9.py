
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                 9: 30, 10: 31, 11: 30, 12: 31}
​
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
​
def add_n_days_to_a_date(date, days):
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])
    for _ in range(days):
        day += 1
        d = days_in_month[month]
        if month == 2 and is_leap_year(year):
            d += 1
        if day > d:
            day = 1
            month += 1
            if month == 13:
                month = 1
                year += 1        
    return str(day).zfill(2) + str(month).zfill(2) + str(year).zfill(4)

