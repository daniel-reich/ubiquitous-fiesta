
def odd_square_patch(lst):
  w = len(lst[0])
  h = len(lst)
  def idx_of(x, y):
    return y * w + x
  lst = [v % 2 for row in lst for v in row]
  if len(lst) == 0:
    return 0
  expanded  = True
  while expanded:
    expanded = False
    for i in range(w - 1):
      for j in range(h - 1):
        if lst[idx_of(i,j)] > 0:
          newSize  = min(lst[idx_of(i+1, j)], lst[idx_of(i+1, j+1)], lst[idx_of(i, j+1)]) + 1
          if newSize > lst[idx_of(i, j)]:
            expanded = True
            lst[idx_of(i, j)] = newSize
  return max(lst)

