
def roundup(x): return int(x) if int(x) == x else int(x) + 1
def DECIMATOR(txt):
  return txt[:-(roundup(len(txt) / 10))]

