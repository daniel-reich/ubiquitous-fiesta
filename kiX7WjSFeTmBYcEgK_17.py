
def major_sum(lst):
    pos_num = 0
    neg_num = 0
    zeroes = 0
    i = 0
    result_nums = []
    for i in range(len(lst)):
        if lst[i] > 0:
            pos_num += lst[i]
        elif lst[i] < 0:
            neg_num += lst[i]
        else:
            zeroes += 1
​
    
    print(zeroes)
    print(pos_num)
    print(neg_num)
    if pos_num > abs(neg_num) >= zeroes:
        return pos_num
    elif pos_num > zeroes >= abs(neg_num):
        return pos_num
    elif zeroes > pos_num >= abs(neg_num):
        return zeroes
    elif zeroes > abs(neg_num) >= pos_num:
        return zeores
    elif abs(neg_num) > zeroes >= pos_num:
        return neg_num
    elif abs(neg_num) > pos_num >= zeroes:
        return neg_num

