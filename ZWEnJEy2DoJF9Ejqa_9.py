
def edabit_in_string(txt):
  for i in 'edabit':
    if i not in txt: return 'NO'
    txt=txt[txt.index(i)+1:]
  return 'YES'

