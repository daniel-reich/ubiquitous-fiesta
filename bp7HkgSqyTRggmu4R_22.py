
def reverse_title(txt):
    c= []
    for a in txt.split():
        c.append(a[0].lower()+a[1:].upper())
    return ' '.join(c)

