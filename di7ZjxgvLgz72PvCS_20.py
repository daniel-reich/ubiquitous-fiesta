
def validate_swaps(lst, txt):
    bool_list=[]
​
    for i in range(len(lst)):
​
        if len(txt) != len(lst[i]):
            bool_list.append(False)
            continue
        times_swapped = 0
        if set(lst[i]) & set(txt) == set(lst[i]) :
            for j in range(len(lst[i])):
                if lst[i][j]!=txt[j]:
                    times_swapped+=1
            if times_swapped == 2:
                bool_list.append(True)
            else:
                bool_list.append(False)
​
        else:
            bool_list.append(False)
    return bool_list

