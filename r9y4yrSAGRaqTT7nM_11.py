
def find_missing(lst):
    try:
        l = [len(i) for i in lst if len(i) > 0 and i != None]
        return list(set(list(range(min(l),max(l)+1))) - set(l))[0]
    except (ValueError,TypeError,IndexError):
        return False

