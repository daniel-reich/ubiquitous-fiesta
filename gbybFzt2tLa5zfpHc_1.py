
def three_sum(lst):
  sets =[]
  for i in range(len(lst)-2):
    for j in range(1+i, len(lst)-1):
      for k in range(1+j, len(lst)):
        if lst[i]+lst[j]+lst[k]==0 and [lst[i], lst[j], lst[k]] not in sets:
          sets.append([lst[i], lst[j], lst[k]])
  return sets

