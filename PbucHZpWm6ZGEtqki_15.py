
def sliding_sum(lst, n, k):
  master_list = []
  for i in range(len(lst)-n+1):
    current_sublist = [ lst[i+j] for j in range(n) ]
    if sum(current_sublist) == k: master_list.append(current_sublist)
  
  return master_list

