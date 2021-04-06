
def flatten(lst):
    if any(type(item) == list for item in lst):
        lst = sum((item if type(item) == list else [item] for item in lst), [])
        return flatten(lst)
    return lst

