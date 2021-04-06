
def keyword_cipher(key, message):
    import string
    from collections import OrderedDict
    alf = list(key) + [x for x in string.ascii_uppercase if x not in key.upper()]
    buf = list(OrderedDict.fromkeys(alf))
    d = dict(zip(string.ascii_uppercase, buf))
    return message.upper().translate(str.maketrans(d)).lower()

