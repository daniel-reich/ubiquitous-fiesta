
def num_of_leapyears(years):
    beg, end = years.split('-')
    return len([y for y in range(int(beg), int(end)+1) if is_leap(y)])
​
​
def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

