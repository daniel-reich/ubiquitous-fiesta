
def first_one(a, b=None, c=None, d=None):
  return a if a else b if b else c if c else d if d else 'not found'

