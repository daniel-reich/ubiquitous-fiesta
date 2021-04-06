
def first_index(hex_txt, needle):
    x = "".join([chr(int(i, 16)) for i in hex_txt.split()])
    return x.index(needle)

