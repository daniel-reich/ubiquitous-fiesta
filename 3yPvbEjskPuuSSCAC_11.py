
def trimmed_averages(lst):
  lst.remove(min(lst))
  lst.remove(max(lst))
  avg = sum(lst)/len(lst)
  return round(avg)

