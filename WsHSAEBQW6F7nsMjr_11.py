
def flatten_the_curve(lst):
  if not lst:
    return []
  mean = round(sum(lst)/len(lst),1)
  return [mean for i in lst]

