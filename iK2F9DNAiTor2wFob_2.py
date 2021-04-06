
def calc(s):
    s = list(map(str,list((map(ord,list(str(s)))))))
    return 6*(''.join(s).count('7'))

