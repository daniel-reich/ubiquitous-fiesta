
def simple_encoder(s):
  s=s.lower()
  res=''
  for x in s:
    if s.count(x)>1:
      res+=']'
    else:
      res+='['
  return res

