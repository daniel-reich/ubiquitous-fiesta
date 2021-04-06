
def trimmed_averages(lst):
  lst.sort()
  lst=lst[1:-1]
  return int(round(sum(lst)/len(lst),0))

