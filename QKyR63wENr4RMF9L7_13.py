
def tweak_letters(txt, lst):
    return ''.join(chr((ord(a) +b -97)%26 +97) for a, b in zip(txt, lst))

