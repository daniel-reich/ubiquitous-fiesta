
def tweet(txt):
    for i in '.,!?':
        txt = txt.replace(i, '')
    txt = txt.split()
    return " ".join([i for i in txt if i[0] == "@" or i[0] == "#"])

