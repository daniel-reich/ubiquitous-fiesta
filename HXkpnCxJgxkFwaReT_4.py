
def count_datatypes (*args):
    order = ["int", "str", "bool", "list", "tuple", "dict"]
    dic = {"int" : 0, "str" : 0, "bool" : 0, "list" : 0, "tuple" : 0, "dict" : 0}
​
    for args in args:
        x = str(type(args))
        dic[(x[8 : -2])] += 1
    
    return [dic.get(i) for i in order]

