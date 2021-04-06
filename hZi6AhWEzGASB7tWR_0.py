
def check(lst):
  if sorted(set(lst)) == lst:
    return 'increasing'
  if sorted(set(lst),reverse=True) == lst:
    return 'decreasing'
  return 'neither'

