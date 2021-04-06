
def first_place(x):
    return None if all(not i.isalpha() for i in x) else [i for i in x if i.isalpha()][-1]

