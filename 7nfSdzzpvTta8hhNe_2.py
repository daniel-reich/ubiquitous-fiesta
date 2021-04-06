
def organize(s):
    lst = s.split(', ')
    return ({'name': lst[0], 'age': int(lst[1]), 'occupation': lst[2]}
            if len(lst) > 2 else dict())

