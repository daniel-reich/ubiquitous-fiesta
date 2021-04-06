
def remove_letters(lst, s):
    [lst.remove(x) for x in s if x in lst]
    return lst

