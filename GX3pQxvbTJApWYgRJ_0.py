
def is_kaprekar(n):
  s = str(n**2)
  l,r = '0'+s[:len(s)//2],s[len(s)//2:]
  return int(l)+int(r) == n

