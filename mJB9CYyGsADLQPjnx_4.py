
def first_non_repeated_character(txt):
    if txt == '': return False
    if len(txt) == 1: return txt
    if txt[0] in txt[1:]:
        return first_non_repeated_character(txt.replace(txt[0],''))
    return txt[0]

