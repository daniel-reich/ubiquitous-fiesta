
def tweak_letters(txt, lst):
    return ''.join(chr((ord(c) - ord('a') + lst[i]) % 26 + ord('a'))
                   for i, c in enumerate(txt))

