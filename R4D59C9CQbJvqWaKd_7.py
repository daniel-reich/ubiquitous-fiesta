
def batting_avg(lst):
    h = sum([h for h, ab in lst])
    ab = sum([ab for h, ab in lst])
    return '{:.3f}'.format(h / ab)[1:]

