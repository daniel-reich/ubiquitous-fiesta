
def shadow_sentence(*sentences):
​
  a, b = map(str.split, sentences)
​
  for i, j in zip(a, b):
    if len(i) != len(j) or set(i).intersection(j):
      return False
  
  return len(a) == len(b)

