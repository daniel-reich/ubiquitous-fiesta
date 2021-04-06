
def max_separator(txt):
  new=[]
  for al in txt:
    if txt.count(al)==2:
      first=txt.index(al)
      second=txt.index(al,first+1)
      new.append(txt[(first):(second+1)])
    elif txt.count(al)>=3:     
      first=txt.index(al)
      second=txt.index(al,first+1)
      third=txt.index(al,second+1)
      new.append(txt[(first):(second+1)])
      new.append(txt[(second):(third+1)])
  if new==[]:
    return([])
  else:
    maxx=max([len(l) for l in new])
    return(sorted(list(set(sub[0] for sub in new if len(sub)==maxx))))

