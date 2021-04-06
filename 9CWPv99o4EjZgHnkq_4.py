
def divide(lst, n):
    count = 0
    add_lst = []
    fin_lst = []
    for i in lst:
        add_lst.extend([i])
        if sum(add_lst) > n:
            fin_lst.append(add_lst[:-1])
            add_lst = [add_lst[-1]]
    fin_lst.append(add_lst)
    return fin_lst

