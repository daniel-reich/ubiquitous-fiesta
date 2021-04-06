
def asc_des_none(lst, s):
    if s == "Des":
        lst = sorted(lst, reverse=True)
    elif s == "Asc":
        lst = sorted(lst, reverse=False)
    return lst

