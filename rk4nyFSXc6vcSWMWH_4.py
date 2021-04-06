
def shared_digits(lst):
  for a,b in zip(lst,lst[1:]):
    if not any(i in str(b) for i in str(a)):
      return False
  return True

