
def first_index(hex_txt, needle):
    konversi = ''.join([chr(int(x, 16)) for x in hex_txt.split()])
    
    return konversi.find(needle)

