
def add_n_days_to_a_date(date, days):
    d, m, y = int(date[:2]), int(date[2:4]), int(date[4:])
    
    for i in range(days):
        feb = 29 if is_leap(y) else 28
        if any([
                (d == feb and m == 2),
                (d == 30 and m in [4, 6, 9, 11]),
                (d == 31 and m in [1, 3, 5, 7, 8, 10, 12])
            ]):
            m += 1
            if m == 13:
                y += 1
                m = 1
            d = 1
        else:
            d += 1
            
    return '{:02d}{:02d}{}'.format(d, m, y)
            
    
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

