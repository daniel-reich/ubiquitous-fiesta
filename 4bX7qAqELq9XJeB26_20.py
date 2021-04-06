
def to_camel_case(txt):
  lis=[]
  if '-' in txt:
    lis = txt.split('-')
  elif '_' in txt:
    lis = txt.split('_')
  for i in range(1,len(lis)):
    if lis[i][0].islower():
      lis[i] = lis[i].capitalize()
  return "".join(lis)

