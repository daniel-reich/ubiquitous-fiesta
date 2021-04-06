
def asc_des_none(lst, s):
    return sorted(lst, reverse=s == 'Des') if s else lst

