
def shared_digits(lst):
  for i in range(len(lst) - 1):
    out = False
    for n in str(lst[i]):
      if n in str(lst[i + 1]):
        out = True
    if not out:
      return False
  return True

