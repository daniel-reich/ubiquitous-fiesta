
def coconut_translator(txt):
    return " ".join("".join(a.upper() if b == "1" else a
                            for a, b in zip("coconuts",
                                            "{:0>8}".format(bin(ord(c))[2:])))
                    for c in txt)

