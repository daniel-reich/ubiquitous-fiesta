
def encrypt(word):
  transtable = str.maketrans('aeou', '0123')
  return word[::-1].translate(transtable) + "aca"

