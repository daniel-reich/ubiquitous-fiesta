
def first_one(*args):
  return next((i for i in args if i), "not found")

