
def news_at_ten(txt, n):
​
    str_1 = ' '* n + txt + ' ' * n
    lst_1 = []
​
    for i in range(len(txt) + n + 1):
        lst_1.append(str_1[:n])
        str_1 = str_1[1:len(txt) + n + 1] + str_1[0]
​
    return lst_1

