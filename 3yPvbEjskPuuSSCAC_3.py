
def trimmed_averages(lst):
  sortlist = sorted(lst)
  trim = sortlist[1:-1]
  return round(sum(trim)/len(trim),0)

