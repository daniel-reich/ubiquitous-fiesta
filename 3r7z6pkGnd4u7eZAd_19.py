
def mark_maths(lst):
  perc = sum(eval(eq.split('=')[0]) == int(eq.split('=')[1]) for eq in lst)/len(lst)
  return '{}%'.format(round(perc*100))

