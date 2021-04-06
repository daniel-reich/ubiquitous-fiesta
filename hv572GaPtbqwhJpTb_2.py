
def elasticize(word):
  def is_even(n):
    return n%2==0
  def first_half(word, n):
    l8rs = {}
    for num in range(n):
      l8rs[num] = word[num] * (num+1)
    return l8rs
  def last_half(word, n):
    l8rs = {}
    y = 1
    while len(word) - y > n-1:
      l8rs[y] = word[len(word)-y]*y
      y += 1
    return l8rs
  def combine(fh, lh):
    lst = []
    for key in sorted(list(fh.keys())):
      lst.append(fh[key])
    for key in reversed(sorted(list(lh.keys()))):
      lst.append(lh[key])
    return lst
​
  if len(word) < 3:
    return word
    
  if is_even(len(word)) == False:
    x = 0
    y = 1
​
    while x != len(word) - y:
      x += 1
      y += 1
    
    middle = x
  else:
    middle = int(len(word)/2)
  
  fh = first_half(word, middle)
  lh = last_half(word, middle)
​
  combined = combine(fh, lh)
​
  return ''.join(combined)

