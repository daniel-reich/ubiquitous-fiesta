
def first_index(hex_txt, needle):
    hex_txt = hex_txt.replace('a3', '7e')
    return bytes.fromhex(hex_txt).decode('utf-8').index(needle)

