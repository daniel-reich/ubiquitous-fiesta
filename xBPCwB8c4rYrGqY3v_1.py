
def missing(lst):
  diffs = [lst[i] - lst[i-1] for i in range(1,len(lst))]
  return lst[diffs.index(max(diffs))] + min(diffs)

