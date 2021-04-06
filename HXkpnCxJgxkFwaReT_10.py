
def count_datatypes(*args):
    i = sum(type(arg) == int for arg in args)
    s = sum(type(arg) == str for arg in args)
    b = sum(type(arg) == bool for arg in args)
    l = sum(type(arg) == list for arg in args)
    t = sum(type(arg) == tuple for arg in args)
    d = sum(type(arg) == dict for arg in args)
    return [i,s,b,l,t,d]

