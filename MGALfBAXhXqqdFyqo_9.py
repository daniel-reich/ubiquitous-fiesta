
def atbash(txt):
    return ''.join(chr(abs((219 if 96 < ord(i) < 123 else 155 if 64 < ord(i) < 91 else 0) - ord(i))) for i in txt)

