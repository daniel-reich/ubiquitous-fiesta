
def coconut_translator(txt):
    x = 'coconuts'
    byte = [bin(ord(b)).replace('b', '').zfill(8) for b in txt]
    return ' '.join([''.join(x[idx].upper() if l == '1' else x[idx] for idx, l in enumerate(word)) for word in byte])

