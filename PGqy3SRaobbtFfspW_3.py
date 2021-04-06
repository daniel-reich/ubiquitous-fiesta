
def simple_pair(lst, n):
  for i in range(len(lst)-1):
    for z in range(i+1, len(lst)):
      if lst[i] * lst[z] == n:
        return [lst[i], lst[z]]

