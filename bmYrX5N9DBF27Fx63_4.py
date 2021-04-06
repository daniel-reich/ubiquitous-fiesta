
def greatest_impact(lst):
    s = [sum(i) for i in zip(*lst)]
    s[2] *= 10/3
    dif = [abs(s[0]-i) for i in s[1:]]
    if dif.count(min(dif)) > 1:
        return 'Nothing'
    return('Weather', 'Meals', 'Sleep')[dif.index(min(dif))]

