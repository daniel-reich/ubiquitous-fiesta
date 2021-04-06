
def is_truthy(val):
  falsy = ('', 0, False, None, [], {})
  return 0 if val in falsy else 1

