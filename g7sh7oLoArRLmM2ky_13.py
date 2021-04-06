
def baconify(msg, mask=None):
    if mask:
        msg = [c for c in msg if c.isalpha() or c == ' ' or c == '.']
        msg = [format(ord(c.lower()) - 97, 'b').zfill(5) for c in msg]
        msg = ['11111' if c == '-1000001' else c for c in msg]
        msg = list(''.join('11110' if c == '-110011' else c for c in msg))
        mask = list(mask)
        msg_index = 0
        for i in range(len(mask)):
            # 1 = l
            # 0 = u
            if mask[i].isalpha():
                try:
                    if msg[msg_index] == '1':
                        mask[i] = mask[i].lower()
                    else:
                        mask[i] = mask[i].upper()
                    msg_index += 1
                except IndexError:
                    pass  # This is for the trailing extra chars at the end of the mask.
        return ''.join(mask)
    else:
        msg = ''.join(c for c in msg if c.isalpha())
        msg = [msg[i:i + 5] for i in range(0, len(msg), 5) if len(msg[i:i + 5]) == 5]
        msg = [int(''.join('0' if c.isupper() else '1' for c in code), 2) + 97 for code in msg]
        msg = [46 if num == 127 else num for num in msg]
        msg = [32 if num == 128 else num for num in msg]
        msg = ''.join(chr(num) for num in msg)
        return msg

