
def true_equations(lst):
    lst2 = []
    for i in range(len(lst)): lst2.append(lst[i]) if eval(lst[i].replace("=","==")) else ""
    return lst2

