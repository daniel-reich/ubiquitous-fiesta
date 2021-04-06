
def fib_str(n, txt):
  firstletter = txt[0]
  secondletter = txt[1]
  fib = {1: firstletter, 2: secondletter}
  for i in range(3,n+1):
    fib[i] = fib[i-1] + fib[i-2]
  emptystring = ''
  for eachkey in fib.keys():
    emptystring += fib[eachkey] + ', '
  return emptystring.strip()[:-1]

