
def check(lst):
  if all(lst[i]<lst[i+1] for i in range(len(lst)-1))==True : return 'increasing'
  elif all(lst[i]>lst[i+1] for i in range(len(lst)-1))==True: return 'decreasing'
  else: return 'neither'

