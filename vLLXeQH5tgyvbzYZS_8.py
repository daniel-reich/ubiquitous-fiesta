
def is_prim_pyth_triple(lst):
    my_list = []
    count = 0
    
    while count < len(lst):
        for i in range(2, lst[count] + 1):
            if lst[count] % i == 0:
                my_list.append(i)
        count += 1
    
    if not sorted(list(set(my_list))) == sorted(my_list):
        return False
    
    lst = sorted(lst)
    return ((lst[0] ** 2) + (lst[1] ** 2)) == (lst[2] ** 2)

