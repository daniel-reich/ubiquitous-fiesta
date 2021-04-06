
def scale_tip(lst):
  l = 0;r = 0
  for i in range(len(lst)):
    if lst[i] != 'I':
      l += lst[i]
    else:
      for j in range(i+1, len(lst)):
        r += lst[j]
      break
  return 'left' if l > r else 'right' if l < r else 'balanced'

