
def fib_str(n, txt):
  for i in range(2, n):
    txt.append(txt[-1]+txt[-2])
  return ', '.join(txt) if n > 0 else txt[0]

