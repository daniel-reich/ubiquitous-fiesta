
def iso_group(l,m=None):
  if m is None:m=[]
  if l:
    if not m:m.append(l[0])
    elif l[0]>m[0]:
      m.clear()
      m.append(l[0])
    elif l[0]==m[0]:
      m.append(l[0])
    return iso_group(l[1:],m)
  else:
    return m[0]if len(m)<2else m

