
def happy_year(year):
    while True:
        year = year + 1
        if len(set([x for x in str(year)])) == 4:
            return year

