
def batting_avg(lst):
    hits = sum(x[0] for x in lst)
    at_bats = sum(x[1] for x in lst)
    average = str( round(hits/at_bats, 3) )[1:]
    if len(average) != 4:
        return average + '0'
    else:
        return average

