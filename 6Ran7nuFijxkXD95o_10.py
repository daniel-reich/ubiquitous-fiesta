
def keyboard_shortcut(txt):
    txt = (txt.replace('Ctrl + C Ctrl + V', '*')
           .replace(' Ctrl + C', '').replace(' Ctrl + V', ''))
    while '*' in txt:
        idx = txt.index('*')
        txt = (txt[: idx] * 2)[:-1] + txt[idx + 1:]
    return txt

