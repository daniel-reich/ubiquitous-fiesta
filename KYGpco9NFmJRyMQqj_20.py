
def min_removals(txt1, txt2):
  
  in_both = []
  
  for l8r in txt1:
    if l8r in txt2:
      in_both.append(l8r)
​
  
  inboth_count = len(in_both)
  txt1count = len(txt1)
  txt2count = len(txt2)
  
  if inboth_count == 0:
    removals = txt1count + txt2count
  else:
    removals = (txt1count - inboth_count) + (txt2count - inboth_count)
  
  return removals

