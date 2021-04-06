
def even_odd_string(txt):
  odd, even = '', ''
  for i, j in enumerate(txt):
    if i % 2 != 0:
      odd += j
    else:
      even += j
  return even + ' ' + odd

