
def atbash(txt):
  cipher = ""
  for i in txt:
    if i.isalpha():
      if i.isupper():
        n = 155
      else:
        n = 219
      cipher += chr(n-ord(i))
    else:
      cipher += i
  return cipher

