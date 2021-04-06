
def keyboard_shortcut(txt):
    res, clipboard = '', ''
    while txt:
        if txt.startswith('Ctrl + C'):
            clipboard = res
            txt = txt[9:]
        elif txt.startswith('Ctrl + V'):
            res += clipboard
            txt = txt[9:]
        else:
            res += txt[0]
            txt = txt[1:]
    return res.rstrip()

