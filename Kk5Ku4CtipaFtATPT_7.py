
def coconut_translator(txt):
    coco = "coconuts"
    trans = lambda char: "".join([coco[ix] if ch == '0' else coco[ix].upper() \
    for ix, ch in enumerate([bd for bd in bin(ord(char))[2:].zfill(8)])])
    return " ".join(trans(ch) for ch in txt)

