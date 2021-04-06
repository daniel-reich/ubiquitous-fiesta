
def shared_digits(lst):
  lst = [str(i) for i in lst]
  for i in range(len(lst)-1):
    if not any(digit in lst[i+1] for digit in lst[i]):
      return False
  return True

