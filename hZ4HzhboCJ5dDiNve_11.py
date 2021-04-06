
def special_reverse_string(txt):
    spaces = [ind for ind, char in enumerate(txt) if char.isspace()]
    new_txt = list(txt.replace(" ", "").lower())[::-1]
    for space in spaces:
        new_txt.insert(space, " ")
    new_txt = [char.upper() if txt[ind].isupper() else char
               for ind, char in enumerate(new_txt)]
    return "".join(new_txt)

