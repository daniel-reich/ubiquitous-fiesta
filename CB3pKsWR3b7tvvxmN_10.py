
def is_palindrome(txt):
  b = []
  a = txt.split()
  print(a)
  for x in a:
    for y in x:
      if y.isalpha() == True:
        b.append(y)
  print(b)
  c = []
  for z in b:
    c.append(z.upper())
  print(c)
  if c == c[::-1]:
    return True
  else:
    return False

