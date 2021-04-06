
def all_about_strings(txt):
  res=[]
  res.append(len(txt))
  res.append(txt[0])
  res.append(txt[-1])
  if(len(txt)%2==0):
    res.append(txt[int(len(txt)/2)-1] + txt[int(len(txt)/2)])
  else:
    res.append(txt[int(len(txt)/2)])
  if(txt.count(txt[1])>1):
    res.append("@ index " + str(txt.index(txt[1],txt.index(txt[1])+1)))
  else:
    res.append("not found")
  return(res)

