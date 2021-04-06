
def censor(s):
    return ' '.join(i if len(i) < 5 else len(i) * '*' for i in s.split())

