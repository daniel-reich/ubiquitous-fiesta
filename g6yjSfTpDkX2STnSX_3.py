
def convert_to_hex(txt):
    a = txt
    b = []
    for i in a:
        b.append(hex(ord(i)))
    return "".join(" ".join(b).split("0x"))

