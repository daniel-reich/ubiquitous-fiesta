
def scale_tip(lst):
  L = sum(lst[i] for i in range(lst.index('I')))
  R = sum(lst[i] for i in range(lst.index('I') + 1, len(lst)))
  return 'left' if L > R else 'right' if L < R else 'balanced'

