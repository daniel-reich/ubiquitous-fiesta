
def edabit_in_string(txt):
  i=0
  for c in txt:
    if c=='edabit'[i]:
      i+=1
    if i>5:
      return 'YES'
  return 'NO'

