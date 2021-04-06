
def rolls(lst):
    lst2 = [lst[0]]
    a = [[lst[i-1], lst[i]] for i in range(1, len(lst))]
    for i in a:
        if i[0] == 1:
            lst2.append(0)
        elif i[0] == 6:
            lst2.append(i[1]*2)
        else: lst2.append(i[1])
    return sum(lst2)

