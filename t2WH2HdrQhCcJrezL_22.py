
def eda_bit(start, end):
    lst1 = []
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            lst1.append('EdaBit')
        elif i % 3 == 0:
            lst1.append('Eda')
        elif i % 5 == 0:
            lst1.append('Bit')
        else:
            lst1.append(i)
    return lst1

