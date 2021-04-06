
def format_ascii(txt, width):
    x=[txt[i:i+width] for i in range(0, len(txt), width)]
    for i in range(len(x)*2-1):
        if i%2!=0:
            x.insert(i,'\n')
    return ''.join(x)

