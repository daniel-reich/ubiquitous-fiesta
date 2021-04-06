
def palindrome_descendant(num):
  n = str(num)
  while len(n) > 1:
    if all(a==b for a,b in zip(n,reversed(n))):
      return True
    n = "".join([str(int(n[i*2])+int(n[1+i*2])) for i in range (len(n)//2)])
  return False

