
def is_polydivisible(n):
 if len(str(n))==1:
  return True
 else:
  i = 1
  while i<=len(str(n)):
    if int(str(n)[:i])%len(str(n)[:i])!=0:
     return False
    else:
     i+=1
 return True
print(is_polydivisible(12))

