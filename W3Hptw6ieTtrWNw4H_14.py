
get_char = lambda r,c: chr(ord('a') + r*5 + c + (1 if r > 1 or (r == 1 and c > 3) else 0))
get_rc = lambda ch: divmod(ord(ch) - ord('a') - (1 if ch > 'i' else 0), 5)
​
def bifid(text):
    if ' ' in text:
        rc = [[],[]]
        for r,c in [get_rc(c) for c in text.lower() if c.isalpha()]:
            rc[0].append(r)
            rc[1].append(c)
        crc, res = rc[0]+rc[1], ''
        return ''.join(get_char(r,c) for r,c in [crc[i:i+2] for i in range(0, len(crc), 2)])
    else:
        crc, tl = [], len(text)
        for r,c in [get_rc(c) for c in text]:
            crc += [r, c]
        return ''.join(get_char(r,c) for r,c in zip(crc[0:tl], crc[tl:]))

