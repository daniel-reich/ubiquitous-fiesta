
def fib_str(n, txt):
  while len(txt) < n:
    txt.append(txt[-1]+txt[-2])
  return ', '.join(txt)

