
def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
​
def days_in_month(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if m == 2:
        return 29 if is_leap_year(y) else 28
    return 30
​
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
    if end_read < start_read:
        return "Invalid meter readings"
    y1, m1, d1 = [int(_) for _ in start_date.split(',')]
    y2, m2, d2 = [int(_) for _ in end_date.split(',')]
    if [y1, m1, d1] > [y2, m2, d2]:
        return "Invalid date"
    days = 0
    while [y1, m1, d1] != [y2, m2, d2]:
        days += 1
        d1 += 1
        if d1 > days_in_month(m1, y1):
            m1 += 1
            d1 = 1
            if m1 > 12:
                y1 += 1
                m1 = 1
    price = (days * stand + (end_read - start_read) * tariff) * 1.05
    return "$" + str(round(price, 2))

