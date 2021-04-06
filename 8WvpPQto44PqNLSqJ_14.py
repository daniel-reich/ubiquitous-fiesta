
def pad(txt: str) -> str:
    if len(txt) == 140:
        return txt
    elif len(txt) % 2 == 1:
        txt += (140 - len(txt) // 2) * 'lo'
        return txt[:140]
    else:
        txt += ' ' + (140 - len(txt) // 2) * 'lo'
        return txt[:140]

