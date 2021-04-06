
def happy_year(year):    
    while True:
        year += 1
        y = sorted(str(year))
        hy = sorted(set(str(year)))
        if y == hy:
            return year

