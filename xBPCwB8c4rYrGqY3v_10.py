
def missing(lst):
  for i in range(1, len(lst)-1):
    if lst[i] - lst[i-1] != lst[i+1] - lst[i]:
      return lst[i+1] - lst[i] + lst[i-1]

