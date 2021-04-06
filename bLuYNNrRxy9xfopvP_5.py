
def yahtzee_score_calc(lst):
  results=[sum([j for j in lst[i]  if j==i+1]) for i in range (6)]
  if sum(results) >=63:
    results.append(35)
  else:
    results.append(0)
  
  f1,f2=([[j for j in lst[i] if lst[i].count(j) >=3] for i in range (6,7)]),\
  ([[j for j in lst[i] if lst[i].count(j) >=4] for i in range (7,8)])
  if len(f1[0]) > 0:
    results.append(sum(lst[6]))
  else:
    results.append(0)
  if len(f2[0]) > 0:
    results.append(sum(lst[7]))
  else:
    results.append(0)
  
  f1=[[j for j in lst[i] if lst[i].count(j) ==3] for i in range (8,9)]
  if len(f1[0]) > 0:
    f2=[[j for j in lst[i] if (lst[i].count(j) ==2 and j!=f1[0][0])]\
    for i in range (8,9)]
    if len (f2[0]) > 0:
      results.append(25)
    else:
      results.append(0)
  else:
    results.append(0)
  
  results.append([30 if (sorted(lst[i])[:-1]==[1,2,3,4] or \
  sorted(lst[i])[:-1]==[2,3,4,5] or sorted(lst[i])[:-1]==[3,4,5,6]) \
  else 0 for i in range (9,10)][0])
  
  results.append([40 if len(set(lst[i]))==5 \
  else 0 for i in range (10,11)][0])
  
  results.append([50 if len(set(lst[i]))==1 \
  else 0 for i in range (11,12)][0])
  
  results.append(sum(lst[12]))
  
  return sum(results)

