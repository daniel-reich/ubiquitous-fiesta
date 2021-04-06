
def find_missing(l):
​
  if not l:
    return False
​
  l = list(map( lambda x: len(x), l ))
​
  if 0 in l:
    return False
​
  return (set(range(min(l),max(l)+1)) - set(l)).pop()

