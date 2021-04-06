
def asc_des_none(lst, s):
    if s== "None":
        return lst
    elif s == "Des":
        return sorted(lst, key = lambda x: -x)
    else:
        return sorted(lst)

