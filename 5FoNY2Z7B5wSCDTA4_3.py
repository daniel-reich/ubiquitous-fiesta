
happy_year = lambda year: year+1 if len(list(set([int(i) for i in str(year+1)]))) == len([int(i) for i in str(year+1)]) else happy_year(year+1)

