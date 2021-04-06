
def reorder_digits(lst, dir):
    for i in range(len(lst)):
        lst[i]=int(''.join(sorted(str(lst[i]),reverse=(dir=='desc'))))
    return lst

