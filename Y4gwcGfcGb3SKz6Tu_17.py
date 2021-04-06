
def max_separator(txt):
  mx = 0
  lst = []
  for i in range(len(txt)):
    for j in range(i+1,len(txt)):
      if txt[i]==txt[j]:
        if len(txt[i:j+1])>mx:
          mx = len(txt[i:j+1])
          lst = [txt[i]]
        elif len(txt[i:j+1])==mx:
          lst.append(txt[i])
        break
  return sorted(lst)

