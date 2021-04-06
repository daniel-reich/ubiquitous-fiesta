
def move(word):
  a = " ".join(word)
  return "".join(chr(ord(i)+1) for i in a.split())

