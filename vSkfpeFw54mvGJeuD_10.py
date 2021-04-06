
def lychrel(n):
  print(n)
  for i in range(500):
    print(n)
    s = str(n)[::-1]
    print("n " + str(n) + " reversed " + s)
    print("comparing " + s[0:len(s)//2] + " with " + s[:-len(s)//2])
    if s[0:len(s)//2] == s[-len(s)//2:]:
      return i
    n = int(s) + n
    print("adding together to get " + str(n))
  return 0

