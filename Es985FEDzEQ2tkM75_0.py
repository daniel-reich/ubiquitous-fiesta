
def caesar_cipher(text, key):
    in_ = 'abcdefghijklmnopqrstuvwxyz'
    out = in_[key:] + in_[:key]
    return text.translate(str.maketrans(in_, out))

