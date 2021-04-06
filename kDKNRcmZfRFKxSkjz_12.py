
def unmix(txt):
  new_txt=''
  if len(txt)%2==0:
    for i in range(len(txt)):
      if i%2==0:
        new_txt+=txt[i+1]
        new_txt+=txt[i]
  elif len(txt)%2>0:
    for i in range(len(txt)-1):
      if i%2==0:
        new_txt+=txt[i+1]
        new_txt+=txt[i]
    new_txt+=txt[-1]
  return new_txt

