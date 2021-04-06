
def tune(lst):
    v = [329.63,246.94,196.00,146.83,110.00,82.41]
    m = []
    for i in range(6):
        if lst[i] == 0:
            m.append(' - ')
        elif lst[i] > v[i]*1.025:
            m.append('+<<')
        elif lst[i] > v[i]*1.005:
            m.append('+<')
        elif lst[i] < v[i]*.975:
            m.append('>>+')
        elif lst[i] < v[i]*.995:
            m.append('>+')
        else:
            m.append('OK')
​
    return m

