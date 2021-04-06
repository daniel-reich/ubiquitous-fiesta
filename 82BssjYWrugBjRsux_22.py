
def index_multiplier(lst):
  return 0 if len(lst) == 0 else sum([i*j for i, j in enumerate(lst)])

