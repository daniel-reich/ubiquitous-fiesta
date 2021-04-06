
def esthetic(num):
    lst_num_bases = []
    for base in range(2, 11):
        num_aux = num
        s = ''
        while num_aux >= base:
            s += str(num_aux - base*(num_aux // base))
            num_aux //= base
            if num_aux < base:
                s += str(num_aux)
        lst_num_bases.append([base, s[::-1]])
    lst_result = []
    for elem in lst_num_bases:
        if all([abs(int(elem[1][i]) - int(elem[1][i+1])) == 1 for i in range(len(elem[1]) - 1)]):
            lst_result.append(elem[0])
    if len(lst_result) == 0:
        return 'Anti-Esthetic'
    return lst_result

