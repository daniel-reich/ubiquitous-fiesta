
def missing(lst):
  num = (lst[-1] - lst[0]) / len(lst)
  for i in range(len(lst)):
    if lst[i] + num != lst[i+1]:
      return lst[i]+ num

