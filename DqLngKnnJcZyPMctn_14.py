
def stock_picker(lst):
  if not lst:
    return 0
  mini = lst[0]
  rec = 0
  for val in lst[1:]:
    rec = max(rec, val-mini)
    mini = min(mini,val)
  return rec or -1

