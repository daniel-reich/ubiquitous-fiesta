
def partition(txt, n):
    result = []
    while txt != '':
        result.append(txt[0:n])
        txt = txt[n:]
    return result

