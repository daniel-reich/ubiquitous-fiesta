
def empty_values(lst):
    r = []
    for i in lst:
        a = type(i)
        if i == None:
            r.append(i)
        elif a == list:
            r.append([])
        elif a == int:
            r.append(0)
        elif a == float:
            r.append(0.0)
        elif a == set:
            r.append(set())
        elif a == tuple:
            r.append(())
        elif a == str:
            r.append("")
        elif a == bool:
            r.append(False)
    return r

