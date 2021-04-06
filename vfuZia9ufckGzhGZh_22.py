
def seq_level(lst):
  difference = lambda x: [x[foo + 1] - x[foo] for foo in range(len(x) - 1)]
  return_lst = ["Linear", "Quadratic", "Cubic"]
  
  for bar in range(3):
    lst = difference(lst)
    if len(set(lst)) == 1:
      return return_lst[bar]
  return None

