
def mystery_func(lst, n):
  ans = []
  for i in range(len(lst)):
      ans.append(lst[i]%n)
  return ans

