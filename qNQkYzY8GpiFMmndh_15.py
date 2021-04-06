
def join(lst):
  out, min_overlap,overlap=lst[0],10**9,0
  out=lst[0]
  for i in range (len(lst)-1):
    overlap=0
    for j in range (min(len(lst[i]),len(lst[i+1]))):
      if lst[i][len(lst[i])-1-j:]==lst[i+1][:j+1]:
        overlap=j+1
        if (overlap < min_overlap):
          min_overlap=overlap
    out+=lst[i+1][overlap:]
  if(min_overlap==10**9):
    min_overlap=0
  return [out, min_overlap]

