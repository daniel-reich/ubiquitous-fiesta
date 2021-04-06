
def sort_dates(lst, mode):
    p = {}
    for l in lst:
        x = l[6:10]+l[3:5]+l[0:2]+l[11:13]+l[14:]
        p[int(x)] = l
    if mode == "ASC":
        return [value for (key, value) in sorted(p.items())]
    else:
        return [value for (key, value) in sorted(p.items(), reverse = True)]

