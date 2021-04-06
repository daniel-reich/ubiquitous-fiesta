
def make_change(c):
  d = {}
  d['q'] = c //25
  d['d'] = (c - (d['q'] * 25))//10
  d['n'] = (c - (d['q'] * 25) - d['d'] *10)//5
  d['p'] = (c - (d['q'] * 25) - d['d'] *10 - d['n'] * 5)
​
  return d

