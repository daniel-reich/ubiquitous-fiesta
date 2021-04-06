
def text_to_number_binary(txt):
    t = txt.split()
    for n,i in enumerate(t):   
        if i.lower() == 'zero':
            t[n] = '0'
        elif i.lower() == 'one':
            t[n] = '1'
        else:
            t[n] = ''
    t = [i for i in t if i != '']
    while len(t) % 8 != 0:
        t.pop()
    return ''.join(t)

