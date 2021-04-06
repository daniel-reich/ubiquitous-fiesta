
def three_sum(lst):
  hmm = []
  if len(lst)<3:
    return hmm
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      for k in range(j+1,len(lst)):
        if lst[i]+lst[j]+lst[k]==0 and [lst[i],lst[j],lst[k]] not in hmm:
          hmm.append([lst[i],lst[j],lst[k]])
  return hmm

