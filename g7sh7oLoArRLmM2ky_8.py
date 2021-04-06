
def baconify(msg: str, mask=None):
    chars = 'abcdefghijklmnopqrstuvwxyz@@@@. '
    result = ''
​
    if not mask:
        bin_stream = ''.join(['1' if c.islower() else '0' for c in msg if c.lower().isalpha()])
        bin_groups = [''.join(bin_stream[i:i + 5]) for i in range(0, len(bin_stream) // 5 * 5, 5)]
        encoded = ''.join([chars[int(x, 2)] for x in bin_groups])
        return encoded
    else:
        msgValidChars = [c for c in msg.lower() if c in chars and c != '@']
        msgBinEncoding = list(''.join([format(chars.index(c), 'b').zfill(5) for c in msgValidChars]))
        for char in mask:
            if char.isalpha() and msgBinEncoding:
                result = result + (char.lower() if msgBinEncoding.pop(0) == '1' else char.upper())
            else:
                result = result + char
        return result

