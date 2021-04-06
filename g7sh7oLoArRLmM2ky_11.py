
def baconify(msg, mask=''):
    chars = 'abcdefghijklmnopqrstuvwxyzFILL. '
    def debacon(key, mask):
        result = ''
        key_alpha = [char for char in key.lower() if char.isalpha() or char == ' ' or char == '.']
        key_indices = [chars.index(char) for char in key_alpha]
        binaries = list(''.join([format(idx,'b').zfill(5) for idx in key_indices]))
        for char in mask:
            if char.isalpha() and binaries:
                result = result + (char.lower() if binaries.pop(0) == '1' else char.upper())
            else:
                result = result + char
        return result
    if mask:
        return debacon(msg, mask)
    else:
        bits = ['1' if char.islower() else '0' for char in msg if char.isalpha()]
        chunks = [bits[chunk:chunk+5] for chunk in range(0,len(bits)-4,5)]
        indices = [int(''.join(chunk),2) for chunk in chunks]
        return ''.join([chars[idx] for idx in indices])

