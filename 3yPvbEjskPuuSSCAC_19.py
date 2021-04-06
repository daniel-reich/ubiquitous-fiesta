
def trimmed_averages(lst):
  length = len(lst)
  lst.sort()
  a = lst[1:length - 1]
  return round(sum(a) / (length - 2), 0)

