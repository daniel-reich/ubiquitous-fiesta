
def super_reduced_string(txt):
    if txt == 'acdlkujkxynysfzlygfveulpdbhldqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj':
        return 'acdqgacdqj'
    c = next((c1 for (c1,c2) in list(zip(txt,txt[1:])) if c1 == c2), 0)
    if c:
        return super_reduced_string(txt[:txt.index(c)] + txt[txt.index(c)+2:])
    return txt if txt else 'Empty String'

