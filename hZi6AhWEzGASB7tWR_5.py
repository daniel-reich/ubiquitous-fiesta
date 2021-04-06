
def check(lst):
  if lst == sorted(set(lst)):
    return 'increasing'
  if lst == sorted(set(lst), reverse=True):
    return 'decreasing'
  return 'neither'

