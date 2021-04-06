
def sum_fractions(lst):
    s=0
    for i in lst :
        d=i[0]/i[1]
        s+=d
    return round(s)

