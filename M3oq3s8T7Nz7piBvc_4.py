
def even_odd_string(txt):
  even, odd = '', ''
  for i in range(len(txt)):
    if i%2 == 0:
      even = even+txt[i]
    else:
      odd = odd+txt[i]
  combined = even + ' ' + odd
  return combined

