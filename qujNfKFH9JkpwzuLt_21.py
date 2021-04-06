
def first_index(hex_txt, needle):
    return bytearray.fromhex(hex_txt).decode('latin1').find(needle)

