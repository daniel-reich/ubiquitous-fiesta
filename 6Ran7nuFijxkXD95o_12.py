
def keyboard_shortcut(txt):
    cache = ""
    for i in range(0,len(txt)):
        if txt[i:i+8] == "Ctrl + C":
            cache = txt[:i]
            txt = txt.replace("Ctrl + C","",1)
        if txt[i:i+8] == "Ctrl + V":
            txt = txt.replace("Ctrl + V",cache,1)
            cache = ""
    return " ".join(txt.split())

