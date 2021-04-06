
def super_reduced_string(txt):
    deleted = True
    while deleted:
        deleted = False
        for i in range(97, 123):
            c = chr(i) * 2
            if c in txt:
                txt = txt.replace(c, '')
                deleted = True
    return txt if txt else 'Empty String'

