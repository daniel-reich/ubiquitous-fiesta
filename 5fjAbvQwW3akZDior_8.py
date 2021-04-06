
def unrepeated(txt):
    msg = ""
    for i in range(len(txt)):
        if not txt[i] in msg:
            msg += txt[i]
    return msg

