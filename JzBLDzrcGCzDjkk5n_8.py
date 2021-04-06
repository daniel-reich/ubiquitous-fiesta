
def encrypt(word):
    word = word[::-1]
    replaces = word.maketrans('aeou', '0123')
    return word.translate(replaces) + 'aca'

