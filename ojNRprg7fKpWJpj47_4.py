
def shift_sentence(a):
    a = a.split()
    new_list = a[:]
    new_list[0] = a[-1][0] + a[0][1:]
    for i in range(1, len(a)):
        new_list[i] = a[i-1][0] + a[i][1:] 
    return " ".join(new_list)

