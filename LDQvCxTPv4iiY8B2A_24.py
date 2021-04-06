
def same_upsidedown(s):
    rev = s[::-1]
    inv = s.replace('6', '_').replace('9', '6').replace('_',  '9')
    return rev == inv

