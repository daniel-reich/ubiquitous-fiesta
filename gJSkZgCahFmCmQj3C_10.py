
def de_nest(lst):
  return eval('lst' + '[0]' * str(lst).count('['))

