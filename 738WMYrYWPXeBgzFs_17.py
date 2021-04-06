
def is_valid(txt):
  txt = list(txt)
  counts = []
  for i in list(set(txt)):
    counts.append(txt.count(i))
  mini = min(counts)
  extra = 0
  for i in counts:
    extra += i - mini
  if extra == 0 or extra == 1:
    return 'YES'
  else:
    return 'NO'

