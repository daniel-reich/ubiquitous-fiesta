
def convert_to_hex(txt):
    txt.lower()
    lst = []
    for i in txt:
        convert = hex(ord(i))
        new_convert = convert.replace('0x', '')
        lst.append(new_convert)
    return ' '.join(lst)

