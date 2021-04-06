
def round_number(num, n):
  m, o = num +0, num + 0
  while m%n and o%n:
    m-=1
    o+=1
  return o if not o%n else m

