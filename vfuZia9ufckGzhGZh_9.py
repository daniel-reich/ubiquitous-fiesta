
def seq_level(lst):
  for i in range(len(lst)-3):
    if lst[i+1] - lst[i] == lst[i+2] - lst[i+1]:
      return 'Linear'
    else:
      if lst[i+3] - lst[i+2] - lst[i+1] + lst[i] == (lst[i+2] - lst[i+1] - lst[i+1] + lst[i]) * 2:
        return 'Quadratic'
  return 'Cubic'

