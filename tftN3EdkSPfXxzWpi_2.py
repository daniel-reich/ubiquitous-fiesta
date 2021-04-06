
def sentence_searcher(txt, n):
  lst = txt[:-1].split('. ')
  i = 0
  if n < 0:
    if 14 + n < 4:
      i = 0
    elif 14 + n > 3 and 14 + n < 8:
      i = 1
    else:
      i = 2
  else:
    if n < 4:
      i = 0
    elif n > 3 and n < 8:
      i = 1
    else:
      i = 2
  return lst[i] + '.'

