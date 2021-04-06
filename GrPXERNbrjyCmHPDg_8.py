
def duplicate_count(txt):
  countDuplicate =0
  
  for char in txt:
    if txt.count(char)>1:
      countDuplicate +=1
      txt = txt.replace(char,'')
  return countDuplicate

