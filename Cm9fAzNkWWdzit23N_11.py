
def wave(txt):
  string_length = len(txt)
  new_string=[]
  sample_string=[]
  null_string=[]
  for char in txt :
    sample_string+=char.upper()
    
  for i,k in enumerate(sample_string):
    if k.lower() == txt[i]:
      new_string.append(txt[:i]+k+txt[i+1:])
      
  for i in new_string:
    if i.islower():
      new_string.remove(i)
    elif i.isspace():
      return []
  return new_string

