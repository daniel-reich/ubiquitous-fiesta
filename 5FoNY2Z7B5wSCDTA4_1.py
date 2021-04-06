
def happy_year(year):
    n = year + 1
    while len(set(str(n))) < 4:
        n += 1
    return n

