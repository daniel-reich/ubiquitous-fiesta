
def mystery_func(txt):
  a = [i for i in txt if i.isalpha()]
  b = [int(i) for i in txt if i.isdigit()]
  return "".join([a[i]*b[i] for i in range(len(a))])

