
def trimmed_averages(lst):
  lst = sorted(lst)
  return round((sum(lst)-lst[0]-lst[-1])/(len(lst)-2),0)

