
def min_length(lst,n):
    len_lst = []
    for i in range(1, len(lst)+1):
        for j in range(len(lst) - i + 1):
            if sum(lst[j:j + i])>n:
                len_lst.append(len(lst[j:j + i]))
    if len(len_lst)==0:
        return -1
    return sorted(len_lst)[0]

