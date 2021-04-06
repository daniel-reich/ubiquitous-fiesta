
def flatten_the_curve(lst):
  return [round(sum(n for n in lst)/len(lst),1) for n in lst] if len(lst) > 0 else lst

