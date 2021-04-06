
def scale_tip(lst):
  return 'right' if sum(lst[(len(lst)+1)//2:]) > sum(lst[:(len(lst)+1)//2-1]) else 'left' if sum(lst[(len(lst)+1)//2:]) < sum(lst[:(len(lst)+1)//2-1]) else 'balanced'

