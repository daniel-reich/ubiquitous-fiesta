
def count_digits(l, t):
  
  d = []
  for n in l:
    num = sum([ 1 for i in str(n) if int(i)%2 ])
    d.append(num if t=='odd' else len(str(n)) - num)
​
  return d

