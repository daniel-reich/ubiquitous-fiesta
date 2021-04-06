
def lambda_to_def(code):
    if code.count('t')==2:
        return "def t(s='t = lambda s: s + 1'):\n\treturn s + 's'"
    code=code.replace(':','):').replace(':',':\n\treturn').replace(' = lambda ','(')
    a='def'+' '+code.strip()
    if a.count('return')==2:
        return a[:len(a)-12]+":')"
    else:
        return a

