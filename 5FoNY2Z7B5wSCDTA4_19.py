
def happy_year(year):
    anul = []
    for i in list(range(year+1, year+100)):
        if len(set([int(x) for x in list(str(i))])) == 4:
            anul.append(i)
    return anul[0]

