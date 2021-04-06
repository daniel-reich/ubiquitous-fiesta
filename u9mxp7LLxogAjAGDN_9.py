
def factor_sort(nums):
  r = []
  for i in nums:
    leni = 0
    for j in range(1, i + 1):
      if i % j == 0:
        leni += 1
    r.append([-leni, -i])
  r.sort()
  return [-k[1] for k in r]

