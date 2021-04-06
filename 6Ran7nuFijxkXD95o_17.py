
def keyboard_shortcut(txt):
    txt = txt.replace("Ctrl + C","#")
    txt = txt.replace("Ctrl + V","*")
    clipboard = ""
    output = ""
    skip = 0
    for index, i in enumerate(txt):
        if skip:
            skip = 0
            continue
        if i == "#":
            clipboard = output
            skip = 1
        elif i == "*":
            output += clipboard
            skip = 1
        else:
            output += i
    return output.strip()

