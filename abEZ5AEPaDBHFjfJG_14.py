
def formula(txt):
    if not txt:
        return None
    txt = txt.replace('=','==')
    if 'a' in txt:
        txt = txt.replace('a','4')
    if eval(txt):
        return True
    return False

