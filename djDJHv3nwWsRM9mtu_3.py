
def validate_spelling(txt):
    c=[]
    a=txt.split('.')
    b=''
    if a[-1]=='':
        for i in a[:-2]:
            b+=(i.lower())
        for i in a[-2]:
            c.append(i)
        if ' '.join(c[1:])==b.capitalize():
            return True
        else:
            return False
    else:
        for i in a[:-1]:
            b+=(i.lower())
        for i in a[-1][:-1]:
            c.append(i)
        if ' '.join(c[1:])==b.capitalize():
            return True
        else:
            return False

