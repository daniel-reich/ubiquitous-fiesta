
def count_datatypes(*args):
    l1 = sum([type(i) == int for i in args])
    l2 = sum([type(i) == str for i in args])
    l3 = sum([type(i) == bool for i in args])
    l4 = sum([type(i) == list for i in args])
    l5 = sum([type(i) == tuple for i in args])
    l6 = sum([type(i) == dict for i in args])
    return [l1, l2, l3, l4, l5, l6]

