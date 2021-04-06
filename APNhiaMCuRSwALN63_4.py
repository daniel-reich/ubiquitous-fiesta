
def almost_palindrome(txt):
  b = 0
  if len(txt) % 2 == 0:
    for i in range(len(txt)//2):
      if txt[i] == txt[len(txt)-i-1]:
        b = b
      else:
        b += 1
      
  if len(txt) % 2 != 0:
    for i in range((len(txt)-1)//2):
      if txt[i] == txt[len(txt)-i-1]:
        b = b
      else:
        b += 1
      
  return b == 1

