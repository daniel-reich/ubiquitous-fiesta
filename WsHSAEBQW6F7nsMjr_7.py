
def flatten_the_curve(lst):
  if lst == []:
    return []
  average = round(sum(lst)/len(lst), 1)
  if average % 1 == 0:
    average = int(average)
  return [average] * len(lst)

