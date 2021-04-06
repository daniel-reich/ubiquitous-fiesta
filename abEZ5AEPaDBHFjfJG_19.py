
def formula(txt):
    if not txt:
        return None
    txt = txt.replace('a', '4')
    x = txt.split('=')
    for i in range(1, len(x)):
        if eval(x[i-1]) != eval(x[i]):
            return False
    return True

