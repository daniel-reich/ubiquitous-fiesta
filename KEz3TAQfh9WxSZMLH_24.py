
def count_all(txt):
  d = {'LETTERS':0, 'DIGITS':0}
  for i in txt:
    if i.isalpha():
      d['LETTERS']+=1 
    elif i.isdigit():
      d['DIGITS']+=1
  return d

