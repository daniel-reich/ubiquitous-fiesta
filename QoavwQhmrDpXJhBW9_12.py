
def flip_list(lst):
    if len(lst)==0:
        return []
    elif isinstance(lst[0], list):
        return [int(str(i)[1:-1]) for i in lst]
    else:
        return [[i] for i in lst]

