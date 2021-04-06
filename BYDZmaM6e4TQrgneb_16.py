
def fibFast(num):
    tab = {0:0, 1:1}
    i = 2
    while(num not in tab):
        tab[i] = tab[i-1] + tab[i-2]
        i += 1
    return tab[num]

