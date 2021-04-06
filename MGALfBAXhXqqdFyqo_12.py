
atbash = lambda s: ''.join(chr(25 - ord(x) + (130 if x.isupper() else 194)) if x.isalpha() else x for x in s)

