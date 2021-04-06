
def flatten_the_curve(lst):
  try:
    x = round(sum(lst)/len(lst),1)
    new = []
    for i in lst:
      new.append(x)
    return new
  except Exception:
    return []

