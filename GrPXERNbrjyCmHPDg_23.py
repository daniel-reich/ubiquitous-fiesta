
def duplicate_count(txt):
  d = {}
  for letter in txt:
    if letter in d:
      d[letter] += 1
    else:
      d[letter] = 1
  
  count = 0
  for i in d:
    if d[i] > 1:
      count += 1
  return count

