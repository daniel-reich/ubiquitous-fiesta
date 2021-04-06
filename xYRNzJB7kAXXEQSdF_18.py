
def wiggle_string(s):
  l = len(s) * 2 + 1
  f1 = [i * " " + s for i in range(0, l//2 + 1)]
  f2 = [i * " " + s for i in range(l//2 - 1, -1, -1)] 
  return f1 + f2

