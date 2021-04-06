
def validate_spelling(txt):
    t = txt.split('. ')
    a = ''.join(t[:-1]).lower()
    b = t[-1][:-1].lower()
    
    return a == b

