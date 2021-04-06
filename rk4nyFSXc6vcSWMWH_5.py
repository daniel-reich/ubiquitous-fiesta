
def shared_digits(lst):
  for pair in zip(lst[::], lst[1::]):
    if not any(ch in str(pair[1]) for ch in str(pair[0])):
      return False
  return True

