
def Kaprekar(n):
  if len(str(n)) == 4 and len(set(str(n))) == 1:
    return prnt([], False)
  return prnt(kpkr(n))
​
def kpkr(n):
  r, k = list(), str()
  while n != 6174:
    a = ''.join(sorted(str(n)+'0'*(4-len(str(n)))))
    b = a[::-1]
    n = int(b) - int(a)
    k = '0'*(4-len(str(n)))+str(n) if len(str(n)) < 4 else str(n)
    r += [[b, a, k]]
  return r
​
def prnt(r, e=True):
  c = ['\n---------- The Mysterious Number 6174 ----------']
  if not e:
    c += ['\nError, n cannot be a repdigit.']
  else:
    c += ['\nNumber of iterations: '+str(len(r)), '\nIterations:\n']
    for i, [a, b, k] in enumerate(r):
      c += ['Iteration Nr. '+str(i+1)+': '+a+' - '+b+' = '+k]
  c += ["\n------------------------------------------------"]
  return '\n'.join(c)

