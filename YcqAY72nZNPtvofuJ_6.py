
def quad_sequence(lst):
  for i in range(len(lst)):
    lst = (lst + [3*lst[-1] - 3*lst[-2]+ lst[-3]])[1:]
  return lst

