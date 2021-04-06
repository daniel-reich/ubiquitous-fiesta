
def baconify(msg, mask=''):
    case = ('uuuuu', 'uuuul', 'uuulu', 'uuull', 'uuluu', 'uulul', 'uullu', 
            'uulll', 'uluuu', 'uluul', 'ululu', 'ulull', 'ulluu', 'ullul', 
            'ulllu', 'ullll', 'luuuu', 'luuul', 'luulu', 'luull', 'luluu', 
            'lulul', 'lullu', 'lulll', 'lluuu', 'lluul', 'llllu', 'lllll')
    chars = 'abcdefghijklmnopqrstuvwxyz. '
    res = []
​
    if mask:
        encrypt = dict(zip(chars, case))
        to_mask = iter(''.join(encrypt.get(i, '') for i in msg.lower()))
​
        for i in mask.lower():
            if i.isalpha():
                try:
                    c = next(to_mask)
                    res.append(i.upper() if c == 'u' else i)
                except StopIteration:
                    res.append(i)
            else:
                res.append(i)
    else:
        msg = ''.join(i for i in msg if i.isalpha())
        decrypt = dict(zip(case, chars))
​
        for i in range(0, len(msg), 5):
            group = ''.join('l' if c.islower() else 'u' for c in msg[i:i+5])
            res.append(decrypt.get(group, ''))
    
    return ''.join(res)

