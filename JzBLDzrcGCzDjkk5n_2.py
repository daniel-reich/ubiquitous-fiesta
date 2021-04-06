
def encrypt(word):
  word = word[::-1]
  for r in (("a", "0"), ("e", "1"), ("o", "2"), ("u", "3")):
    word = word.replace(*r)
    
  return word+'aca'

