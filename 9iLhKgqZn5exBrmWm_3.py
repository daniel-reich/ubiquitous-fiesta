
def ascending(txt):
  for i in range(1,len(txt)//2+1):
    k,B,C=0,[],[]
    for j in range(len(txt)):
      if len(txt[k:k+i])==i and len(txt[k+i:k+2*i])==i:
        C.append([txt[k:k+i],txt[k+i:k+2*i]])
        B.append(int(txt[k:k+i])+1==int(txt[k+i:k+2*i]))
        k=k+i
    if all(B) and C[-1][-1][-1]==txt[-1]:
      return True
      break
  else:
    return False

