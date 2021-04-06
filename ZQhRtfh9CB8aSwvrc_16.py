
def greater_than_sum(lst):
  return all([sum(lst[:i])<lst[i] for i in range(1,len(lst))])

