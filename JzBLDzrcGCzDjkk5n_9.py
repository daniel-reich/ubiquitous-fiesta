
def encrypt(word):
  return "".join(str("aeou".index(i)) if i in "aeou" else i for i in word[::-1])+"aca"

