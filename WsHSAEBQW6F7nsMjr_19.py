
def flatten_the_curve(lst):
  return lst if not lst else [round(sum(lst)/len(lst), 1)] * len(lst)

