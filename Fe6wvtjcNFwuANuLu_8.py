
def ping_pong(lst, win):
    new = []
    for i in lst:
        new.append(i)
        new.append('Pong!')
    if win == False:
        return new[:-1]
    else:
        return new

