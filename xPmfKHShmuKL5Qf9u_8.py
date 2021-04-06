
def scale_tip(lst):
  return "left" if sum(lst[:(len(lst)-1)//2]) > sum(lst[(len(lst)-1)//2+1:]) else "right"\
  if sum(lst[:(len(lst)-1)//2]) < sum(lst[(len(lst)-1)//2+1:]) else "balanced"

