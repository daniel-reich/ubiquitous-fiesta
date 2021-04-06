
def convert_to_hex(txt):
    return ''.join([hex(ord(char))[2:] + ' ' for char in txt])[:-1]

