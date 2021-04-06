
def check(lst):
  if len(set(lst)) < len(lst):
    return 'neither'
  return 'increasing' if lst == sorted(lst) else 'decreasing'

