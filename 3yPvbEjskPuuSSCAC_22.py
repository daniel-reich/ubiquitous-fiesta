
def trimmed_averages(lst):
  lst = sorted(lst)
  lst.remove(max(lst))
  lst.remove(min(lst))
  return round(sum(lst)/len(lst))

