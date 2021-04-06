
def encrypt(word):
  a = str.maketrans("aeou", "0123")
  return word[::-1].translate(a) + "aca"

