
def longest_7segment_word(lst):
  let = 'kmvwx'
  m = list(filter(lambda x: not any(l in x for l in let),lst))
  return max(m,key=len) if m else ''

