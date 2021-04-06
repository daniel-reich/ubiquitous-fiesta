
def longest_7segment_word(lst):
  flt=[]
  for i in lst:
    if all(j not in 'kmvwx' for j in i):
      flt.append(i)
  try:
    return sorted(flt, key=len, reverse=True)[0]
  except:
    return ''

