
def is_truthy(val):
  falsy = [None, False, 0, {}, [], ""]
  return 0 if val in falsy else 1

