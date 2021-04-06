
def is_valid_date(d, m, y):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y%4==0 and (y%100 != 0 or y%400==0):
        day_count_for_month[2] = 29
    return (1 <= m <= 12 and 1 <= d <= day_count_for_month[m])

