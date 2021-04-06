
def find_the_falsehoods(lst):
    new_lst = []
    for x in lst:
        if not x:
            new_lst.append(x)
    return new_lst

