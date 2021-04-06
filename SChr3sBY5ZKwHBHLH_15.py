
def sort_it(lst):
    return sorted(lst, key=get_key)
​
def get_key(x):
    if type(x) == list:
        return x[0]
    return x

