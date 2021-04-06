
def simple_equation(a, b, c):
​
    import itertools
​
    operators = ['+', '-', '*', '/']
    lst_1, lst_2, lst_3 = [a, b, c], [], []    
    perm = itertools.permutations(lst_1)
​
    for i in list(perm):
        lst_2.append(list(i))   
​
    for x in lst_2:
        for y in operators:
            if eval(str(x[0]) + y + str(x[1])) == x[2]:
                lst_3.append((str(x[0]) + y + str(x[1]) + '=' + str(x[2])))
​
    if len(lst_3) == 0:
        return str("")
    else:
        return lst_3[0]

