
def is_kaprekar(n):
  s = str(n*n)
  s = '0' * (len(s)%2) + s
  return int(s[:len(s)//2]) + int(s[len(s)//2:]) == n

