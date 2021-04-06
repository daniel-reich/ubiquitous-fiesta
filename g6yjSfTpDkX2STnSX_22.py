
def convert_to_hex(txt):
    o_txt = ""
    for i in txt:
        o_txt += hex(ord(i)) + " "
    return o_txt.replace("0x", "")[:-1]

