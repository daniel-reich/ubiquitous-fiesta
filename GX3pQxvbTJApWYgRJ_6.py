
def is_kaprekar(n):
  m = str(n**2)
  left = '0'+m[:len(m)//2]
  right = m[len(m)//2:]
  return n == int(left) + int(right)

