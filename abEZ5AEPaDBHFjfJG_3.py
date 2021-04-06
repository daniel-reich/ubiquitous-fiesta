
def formula(txt):
    return eval(txt.replace('=', '==').replace('a', '4')) if txt else None

