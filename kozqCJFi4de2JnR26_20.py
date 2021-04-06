
def fib_str(n, txt):
  for i in range(n-2):
    txt.append(txt[i+1]+txt[i])
  return ', '.join(txt)

