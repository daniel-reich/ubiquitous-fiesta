
def first_non_repeated_character(txt):
  x =0
  w =len(txt)
  for i in txt:
    x +=1
    if txt.count(i)==1:
      return (i)
  
  return (False)

