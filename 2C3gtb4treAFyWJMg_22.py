
a = ord('a')
z = ord('z')
zero = ord('0')
nine = ord('9')
​
def get_index(n):
  index = n-a
  if index > 8:
    index -= 1
  return "%s%s" %(1+int(index/5),1+index%5)
  
def get_letter(r,c):
  index = (r-1)*5+(c-1) 
  if index > 8:
    index += 1
  index += a
  return chr(index)
  
def polybius(text):
  text = text.lower()
  res = ''
  r = None
  c = None
  for t in text:
    n = ord(t)
    if n >= a and n <= z:
      res += get_index(n)
    elif n >= zero and n <= nine:
      if r == None:
        r = int(t)
      elif c == None:
        c = int(t)
        res += get_letter(r,c)
        r = None
        c = None
    elif t == " ":
      res += t
  return res

