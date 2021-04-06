
def merge(a, b):
    int_len = max(len(a), len(b))
    arr_res = []
    
    for idx, item in enumerate(b):
        idx_upper_1 = idx-1 if idx -1 >= 0 else idx 
        idx_upper_2 = idx if idx <= len(a)-1 else idx-1 
        arr_res.append(max(item + a[idx_upper_1], item + a[idx_upper_2]))
    return arr_res
        
​
def longest_slide(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]
    
    temp = merge(pyramid[0], pyramid[1])
    for i in range(2,len(pyramid)):
        temp = merge(temp, pyramid[i])
    return max(temp)

