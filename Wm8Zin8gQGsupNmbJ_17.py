
def binary_conversion(txt):
    lst = []
    a = 0
    b = 8
    for x in range(0, len(txt), 8):
        lst.append(chr(int(txt[a:b], 2)))
        a = a + 8
        b = b +8
    return "".join(lst)

