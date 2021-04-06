
def single_occurrence(txt):
  num = 0
  txt = txt.upper()
  if txt == '': return ''
  for one in txt:
    for test in txt:
      if one == test : num +=1
      
    if num == 1:
      return one
    num = 0

