
def num_of_leapyears(years):
    lst = [int(i) for i in years.split('-')]
    leapyears = 0
    x = lst[1] - lst[0]
    first_year = lst[0]
    for i in range(x + 1):
        if first_year % 4 == 0:
            leapyears = leapyears + 1
            if first_year % 100 == 0 and first_year % 400 != 0:
                leapyears -= 1
        first_year += 1
    return leapyears

