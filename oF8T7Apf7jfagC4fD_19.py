
def antipodes_average(lst):
  d = 1 if len(lst) % 2 == 1 else 0
  f1 = [lst[i] for i in range(0, len(lst)//2)]
  f2 = [lst[i] for i in range(len(lst)//2 + d, len(lst))][::-1]
  ans = []
  for i,j in enumerate(f2):
    ans.append((j + f1[i])/2)
  return ans

