
def symb(x):
  if not x: return '@'
  return 'o'*(x%5)+'-'*(x//5)
​
def maya_number(n):
  r=[n%20] ; n//=20
  while n: r.append(n%20) ; n//=20
  return [symb(i) for i in reversed(r)]

