
def widen_streets(lst, n):
  i = 1
  while i < len(lst[0]) :
    if lst[-1][i-1:i+2] == "# #" :
      for j in range(len(lst)) :
        lst[j] = lst[j][:i] + (" " * n) + lst[j][i+1:]
    i += 1
  return lst

