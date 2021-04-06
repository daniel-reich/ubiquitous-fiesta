
def pyramidal_string(string, ttpe):
  lst=[1,3,6,10,15,21,28]
  result=[]
  if ttpe=="REG":
    if string=='':
      return []
    if len(string) not in lst:
      return "Error!"
    else:
      x=lst.index(len(string))
      for i in range(1,x+2):
        result.append(' '.join(string[:i]))
        string=string[i:]
      return result
  else:
    if len(string)==1:
      return [string]
    if len(string) not in lst:
      return "Error!"
    else:
      x=lst.index(len(string))
      for i in range(x+1,0,-1):
        result.append(' '.join(string[:i]))
        string=string[i:]
      return result

