
def landscape_type(lst):
  if [lst[i-1] < lst[i] and lst[i] > lst[i+1] for i in range(1, len(lst)-1)].count(True) == 1 and lst[0]<=lst[1] and lst[-2]>=lst[-1]: return 'mountain'
  if [lst[i-1] > lst[i] and lst[i] < lst[i+1] for i in range(1, len(lst)-1)].count(True) == 1 and lst[0]>=lst[1] and lst[-2]<=lst[-1]: return 'valley'
  return 'neither'

