
def flip_list(lst):
    try:
        if type(lst[0]) is list:
            return [i[0] for i in lst]
        elif type(lst[0]) is int:
            return [[i] for i in lst]
    except IndexError:
        return []

