
def longest_7segment_word(lst):
  a = 'kmvwx'
  b = []
  for x in lst:
    if 'k' not in x and 'm' not in x and 'v' not in x and 'w' not in x and 'x' not in x:
      b.append(x)
    else:
      pass
  if b == []: 
    return ''
  return max(b, key = len)

