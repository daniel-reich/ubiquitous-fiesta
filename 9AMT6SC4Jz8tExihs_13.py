
def b(n):
  s = ""
  if n < 2: return str(n)
  else:
    while n>0:
      s += str(n%2)
      n //= 2
    return s[::-1]
​
def generate_nonconsecutive(n):
  s = "0"*(n-1) + b(0)
  for _ in range(1, 2**n):
    if "11" not in b(_):
      s += " " + "0"*(n-len(b(_))) + b(_)
  return s

