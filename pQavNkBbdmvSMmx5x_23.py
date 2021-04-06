
def majority_vote(lst):
  unique=list(set(lst))
  if len(unique) == 1: return lst[0]
  if len(unique) == 0: return None
  unique_count=[]
  for i in range(len(unique)):
    unique_count.append(lst.count(unique[i]))
    sorted_list=sorted(unique_count, reverse=True)
  if sorted_list[0] == sorted_list[1]: return None
  local_max=max(unique_count)
  index=unique_count.index(max(unique_count))
  return unique[index]

