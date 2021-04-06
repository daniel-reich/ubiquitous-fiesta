
def larger_than_right(lst):
    my_list = []
    flag = True
    
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if not lst[i] > lst[j]:
                flag = False
                break
        if flag:
            my_list.append(lst[i])
        flag = True
    return my_list

