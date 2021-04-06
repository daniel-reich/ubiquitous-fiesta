
def magic(txt):
  a, b, c = txt.split()
  a , b = int(a), int(b)
​
  return (a * b == int(c[-1])) or (a * b == int(c[-2:]) or (a *b == int(c[1:])))

