
def fib_str(n, f):
  if n==2:
    s = ""
    for x in f:
      s+=str(x)+", "
    return s[:-2]
  else:
    f.extend([f[-1],f[-1]+f[-2]][1:])
    return fib_str(n-1, f)

