
def encrypt(word):
  return word[::-1].replace("a","0").replace("e","1").replace("o","2").replace("u","3") + "aca"

