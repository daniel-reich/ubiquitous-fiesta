
def esthetic(num):
  return [b for b in range(2,11) if check(num,b)] or 'Anti-Esthetic'
​
def check(n,b):
  return n//b==0 or abs(n%b-n//b%b)==1 and check(n//b,b)

