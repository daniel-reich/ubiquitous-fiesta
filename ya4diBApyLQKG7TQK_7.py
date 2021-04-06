
def validate_relationships(txt):
    idx = 1
    while idx < len(txt) - 1:
        if (txt[idx] == '=' and txt[idx - 1].isdigit()
                and (txt[idx + 1].isdigit() or txt[idx + 1] == '-')):
            txt = txt[: idx] + '==' + txt[idx + 1:]
            idx += 1
        idx += 1
    return eval(txt)

