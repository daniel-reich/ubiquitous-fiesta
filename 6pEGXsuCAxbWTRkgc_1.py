
def loves_me(n):
  a=["Loves me"+" not"*(i%2) for i in range(n)]
  a[-1]=a[-1].upper()
  return ", ".join(a)

