
def shift_sentence(txt: str) -> str:
    if txt.find(' ') == -1:
        return txt
    l1 = txt.split()
    l2 = l1[:] * 2
    l2 = l2[len(l1) - 1:]
    for i in range(len(l1)):
        if len(l1[i]) > 1:
            l1[i] = l2[i][0] + l1[i][1:]
        else:
            l1[i] = l2[i][0]
    return ' '.join(l1)

