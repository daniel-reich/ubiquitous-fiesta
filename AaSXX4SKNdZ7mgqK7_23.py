
def first_one(a, b=None, c=None, d=None):
  if a or b or c or d:
    return a or b or c or d
  else:
    return 'not found'

