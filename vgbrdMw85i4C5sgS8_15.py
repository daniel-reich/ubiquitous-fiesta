
def skip_the_sugar(drinks):
  unwanted = {'cola', 'fanta'}
  return [e for e in drinks if e not in unwanted]

