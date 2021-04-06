
def is_palindrome(txt):
  x = int(len(txt)/2)
  w=[]
  y=[]
  for i in range(0,x):
    w += [ord(txt[i])]
  for i in range(0,x):
    txt1 = txt[::-1]
    y += [ord(txt1[i])]
  if sum(w) == sum(y):
    return True
  else:
    return False

