
def first_one(a, b=None, c=None, d=None):
  ris = a or b or c or d
  return ris or 'not found'

