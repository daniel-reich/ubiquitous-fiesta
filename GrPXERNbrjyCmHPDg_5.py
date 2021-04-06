
def duplicate_count(txt):
  sum = 0
  for i in txt:
    if txt.count(i)>=2:
      sum += 1
      txt = txt.replace(i, '')
  return sum

