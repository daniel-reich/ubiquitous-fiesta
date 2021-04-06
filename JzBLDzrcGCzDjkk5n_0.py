
def encrypt(word):
  return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'

