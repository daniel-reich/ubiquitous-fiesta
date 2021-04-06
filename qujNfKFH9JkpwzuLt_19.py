
def first_index(hex_txt, needle):
    lst = hex_txt.split(' ')
    target = hex(ord(needle[0]))[2:]
    return lst.index(target)

