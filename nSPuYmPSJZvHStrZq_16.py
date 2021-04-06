
def oddeven(lst):
    odd_num = []
    even_num = []
    for i in lst:
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    return len(odd_num) > len(even_num)

