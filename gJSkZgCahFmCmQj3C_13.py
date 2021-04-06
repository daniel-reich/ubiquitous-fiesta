
def de_nest(lst):
    while True:
        if type(lst[0]) == list:
            lst = lst[0]
        else:
            return lst[0]

