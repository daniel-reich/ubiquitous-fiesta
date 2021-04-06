
def shhh(txt):
    try:
        first = txt[0]
        rest = txt[1:]
        final = first.upper() + rest.lower()
    except IndexError:
        final = ""
    return '"' + final + '"' + ", whispered Edabit."

