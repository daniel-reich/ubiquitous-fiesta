
def flatten_the_curve(lst):
  return [] if not lst else [round(sum(lst)/len(lst), 1)]*len(lst)

