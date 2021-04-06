
def id_mtrx(n):
    if not isinstance(n, int):
        return 'Error'
    if n < 0:
        new_n = -n
    else:
        new_n = n
​
    final = []
    for x in range(new_n):
        iter_ = 0
        current = []
        while iter_ < x:
            current.append(0)
            iter_ += 1
        current.append(1)
        myiter = new_n - x
        while myiter > 1:
            current.append(0)
            myiter -= 1
            
        final.append(current)
    if n < 0:
        final.reverse()
    return final

