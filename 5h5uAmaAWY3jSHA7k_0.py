
def landscape_type(lst):
  if any((sorted(lst[:i+1]) == lst[:i+1] and sorted(lst[i:], reverse=True) == lst[i:]) for i in range(1,len(lst)-1)):
    return 'mountain'
  elif any((sorted(lst[:i+1], reverse=True) == lst[:i+1] and sorted(lst[i:]) == lst[i:]) for i in range(1,len(lst)-1)):
      return 'valley'
  return 'neither'

