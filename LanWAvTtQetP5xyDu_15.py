
def coins_div(lst):
    if sum(lst)% 3 != 0: return False
    summ = sum(lst)/3
    if max(lst) > summ: return False
    
    lst = sorted(lst, reverse=True)
​
    ks_1 = 0
    ks_2 = 0
    ks_3 = 0
    ks_1c = []
    ks_2c = []
    ks_3c = []
​
    ks_1 = lst[0]
    ks_1c.append(lst[0])
    lst.remove(lst[0])
    if lst[0] == summ and lst[1] == summ: return True
    
    i = 0
    while ks_1 < summ:
        print(i)
        print(lst)
        if lst[i] + ks_1 <= summ:
            ks_1 = lst[i] + ks_1
            ks_1c.append(lst[i])
            print(ks_1c)
            lst.remove(lst[i])
        if i < len(lst)-1: i += 1    
        else: break
    if ks_1 != summ: return False
    
    ks_2 = lst[0]
    ks_2c.append(lst[0])
    lst.remove(lst[0])
    i = 0
    while ks_2 < summ:
        if lst[i] + ks_2 <= summ:
            ks_2 = lst[i] + ks_2
            ks_2c.append(lst[i])
            lst.remove(lst[i])
        if i < len(lst)-1: i += 1
        else: break    
    if ks_1 != summ: return False
    
    ks_3 = sum(lst)
    ks_3c = lst
    
​
    
    print('Final allocation:')
    print(ks_1c)
    print(ks_2c)
    print(ks_3c)
    return True

