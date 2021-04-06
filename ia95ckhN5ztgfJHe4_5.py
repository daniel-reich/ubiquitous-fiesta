
def comments_correct(txt):
    if len(txt) % 2 != 0:
        return False
    lst = []
    c = ''
    for l in txt:
        c += l
        if len(c) == 2:
            lst.append(c)
            c = ''
    if lst[0] == '*/':
        return False
    print(lst)
    for i in range(len(lst)):
        if lst[i] == '*/':
            continue
        elif lst[i] == '/*':
            if lst[i+1] == '*/':
                continue
            else:
                return False
    return True

