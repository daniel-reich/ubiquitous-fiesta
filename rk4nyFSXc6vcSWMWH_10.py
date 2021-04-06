
def shared_digits(lst):
  for a, b in zip(lst[:-1], lst[1:]):
    if not set(str(a)) & set(str(b)):
      return False
  return True

