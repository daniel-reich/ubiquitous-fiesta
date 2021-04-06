
def pyramidal_string(string, _type):
  res=[];c=0
  _type=1 if _type=='REG' else -1
  string=string[::_type]
  while string:
    c+=1
    res+=[' '.join(string[:c])[::_type]]
    string=string[c:]
  if not res:return res
  return "Error!" if len(res[-1])!=c*2-1 else res[::_type]

