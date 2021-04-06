
def numbers_need_friends_too(n):
​
    lst_1 = list(str(n))
    lst_2, lst_3 = [], []
​
    for i in range(len(lst_1) - 1):
        if lst_1[i] != lst_1[i+1]:
            lst_2.append(lst_1[i])
            lst_2.append(',')
        else:
            lst_2.append(lst_1[i])
    lst_2.append(lst_1[-1])
​
    lst_2 = ''.join(lst_2).split(',')
​
    for i in lst_2:
        if len(i) == 1:
            lst_3.append(i * 3)
        else:
            lst_3.append(i)
​
    return int(''.join(lst_3))

