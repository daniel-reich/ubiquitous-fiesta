
def fib_str(n, txt):
  for i in range(n-2):
    txt.append(txt[-1]+txt[-2])
  return ', '.join(txt)

