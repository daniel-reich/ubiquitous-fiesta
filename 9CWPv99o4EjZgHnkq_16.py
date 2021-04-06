
def divide(lst, n):
    res = []
    cur_sub_list = []
    for x in lst:
        if sum(cur_sub_list) + x <= n:
            cur_sub_list.append(x)
        else:
            res.append(cur_sub_list)
            cur_sub_list = [x]
    if len(cur_sub_list): 
        res.append(cur_sub_list)
    return res

