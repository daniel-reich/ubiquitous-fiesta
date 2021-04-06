
def leap_year(y):
    return y%400 == 0 or (y%4 == 0 and y%100 != 0)
​
def days_between_dates(date1, date2):
    date1, date2 = sorted((date1, date2), key=lambda x: int(x[-4:] + x[2:4] + x[:2]))
    d1, m1, y1 = int(date1[:2]), int(date1[2:4]), int(date1[-4:])
    d2, m2, y2 = int(date2[:2]), int(date2[2:4]), int(date2[-4:])
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    months[1] = 29 if leap_year(y2) else 28
    partial_1 = d2 if m2 == 1 else sum(months[:m2-1]) + d2
    months[1] = 29 if leap_year(y1) else 28
    partial_2 = sum(months[m1-1:]) - d1
    year_days = sum(366 if leap_year(y) else 365 for y in range(y1+1, y2))
    total = partial_1 + partial_2 + year_days
    
    if y1 == y2:
        return total - 366 if leap_year(y1) else total - 365
    return total

