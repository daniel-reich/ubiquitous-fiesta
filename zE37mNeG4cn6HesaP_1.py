
def index_letter(word):
  for index, letter in enumerate(word):
    yield index, letter
    
def distance(x, y):
  return sum(
  i != j
  for i, j in zip(index_letter(x), index_letter(y))
  )
​
def max_ham(s1, s2):
  if not sorted(s1) == sorted(s2):
    return False
  else:
    d = distance(s1, s2)
    if d is len(s1):
      return True
    else:
      return d

