
def is_good_match(lst):
  lg = len(lst)
  if lg&1:
    return 'bad match'
  return [lst[i]+lst[i+1] for i in range(0,lg,2)]

