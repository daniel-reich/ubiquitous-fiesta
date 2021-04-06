
def encrypt(word):
  x=''
  a={'a':0,'e':1,'i':2,'o':2,'u':3}
  for i in word:
    if i in a:
      x+=str(a[i])
    else:
      x+=i
  return x[::-1]+"aca"

