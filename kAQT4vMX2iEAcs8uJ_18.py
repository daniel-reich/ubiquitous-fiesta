
def longest_7segment_word(lst):
  res = ''
  banned_chars = 'kvwmx'
  
  for i in lst:
    if len(i) > len(res) and all(ch not in i for ch in banned_chars):
      res = i
      
  return res

