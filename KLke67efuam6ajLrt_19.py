
def shuffle_count(n):
    lst = [a for a in range(1, n + 1)]
    copy_of_lst = lst[:]
    odd_index_ind = n // 2
    even_index_ind = 1
    counter = 1
    temp = [0 for _ in range(n)]
    for i in range(n):
        if not i or i == n - 1:
            temp[i] = lst[i]
            continue
        if i % 2 == 1:
            temp[i] = lst[odd_index_ind]
            odd_index_ind += 1
        elif i % 2 == 0:
            temp[i] = lst[even_index_ind]
            even_index_ind += 1
    lst = temp[:]
    while lst != copy_of_lst:
        odd_index_ind = n // 2
        even_index_ind = 1
        for i in range(n):
            if not i or i == n - 1: 
                continue
            if i % 2 == 1:
                temp[i] = lst[odd_index_ind]
                odd_index_ind += 1
            else:
                temp[i] = lst[even_index_ind]
                even_index_ind += 1
        lst = temp[:]
        counter += 1
    return counter

