
def landscape_type(lst):
  for i in range(1, len(lst)-1):
    lfttop = False
    rghttop = False
    for j in range(0,i-1):
      if lst[j]>lst[j+1]:
        lfttop = True
        break
    if lfttop == False:
      for k in range(i,len(lst)-1):
        if lst[k]<lst[k+1]:
          rghttop = True
          break
    if lfttop == False and rghttop == False:
      if lst[0]==max(lst) or lst[len(lst)-1]==max(lst): return "neither"
      return "mountain"
​
  for i in range(1, len(lst)-1):
    lfttop = False
    rghttop = False
    for j in range(0,i-1):
      if lst[j]<lst[j+1]:   
        lfttop = True
        break
    if lfttop == False:
      for k in range(i,len(lst)-1):
        if lst[k]>lst[k+1]:
          rghttop = True
          break
    if lfttop == False and rghttop == False:
      if lst[0]==min(lst) or lst[len(lst)-1]==min(lst): return "neither"
      return "valley"
  return "neither"

