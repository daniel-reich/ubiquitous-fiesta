
def pilish_string(txt):
  idx=0;mem=[]
  for i in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]:
    if txt[idx:idx+i]:mem+=[txt[idx:idx+i]+txt[idx:idx+i][-1]*(i-len(txt[idx:idx+i]))]
    else:break
    idx=idx+i
  return ' '.join(mem)

