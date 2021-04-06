
def first_index(hex_txt, needle):
    return bytearray.fromhex(hex_txt).decode('ISO-8859-1').index(needle)

