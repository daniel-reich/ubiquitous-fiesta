
def correct_sentences(s):
    for i in range(6):
        s = s.replace('  ',' ')
    if s[-1] == ' ':
        s = s[:-1]
    s += '..'
​
    a = ''
    for i in range(1,len(s)-1):
        if s[i+1].isupper():
            a += '.'+s[i]
        else:
            a += s[i]
    s = ''
    for i in range(len(a)):
        if i == 0:
            s += a[i].upper()
        else:
            s += a[i]
    return s

