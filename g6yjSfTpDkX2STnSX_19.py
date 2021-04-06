
def convert_to_hex(txt):
    thing = [hex(ord(char)) for char in txt]
    hexStr = "".join(char[2:]+ " " for char in thing)
    return hexStr[:-1]

