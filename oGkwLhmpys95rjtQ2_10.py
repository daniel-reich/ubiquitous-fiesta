
def match_last_item(lst):
    new = ''
    for l in lst[:-1]:
        if type(l) != str:
            l = str(l)
        new += l
    return new == lst[-1]

