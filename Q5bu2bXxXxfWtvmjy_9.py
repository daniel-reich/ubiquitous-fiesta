
def missing_letter(txt):
    s = [ord(str(ch)) for ch in txt]
    t = ([x for x in range(s[0], s[-1]+1) if x not in s])
    return ''.join(list(map(chr, t))) or 'No Missing Letter'

