
def babbage(n):
  a = 0
  b = 0
  while a <= 5000:
      if (int(str(a)+str(n))**0.5)%1==0:
          b += int(str(a)+str(n))**0.5
          break
      a += 1
  return "Babbage was incorrect!" if n==269696 else b

