
def longest_run(lst):
  lr = 1
  cr = [1, 1]
  for i in range(1, len(lst)):
    d = lst[i] - lst[i-1]
    if d == cr[1]:
      cr[0] += 1
    else: 
      lr = max(cr[0], lr)
      cr = [2, d] if abs(d) == 1 else [1,1]
  return max(lr, cr[0])

