
def word_to_decimal(word):
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    word = word.lower()[::-1]
    base = ord(max(word)) - 86
    return sum(chars.index(i)*base**idx for idx, i in enumerate(word))

