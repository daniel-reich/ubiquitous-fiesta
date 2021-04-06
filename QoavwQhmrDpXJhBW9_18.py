
def flip_list(lst):
    return [[i] for i in lst] if all([type(i)!=list for i in lst]) else [j for i in lst for j in i]

