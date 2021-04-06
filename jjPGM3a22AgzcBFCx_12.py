
def decrypt(lst):
  x=0
  for i in range(1,27):
    if i not in lst:
      x=i
      return chr(x+64)

