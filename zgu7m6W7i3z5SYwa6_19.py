
def is_equal(lst):
  sumA = sum([int(a) for a in str(lst[0])])
  sumB = sum([int(a) for a in str(lst[1])])
  if sumA==sumB:
      return True
  else:
      return False

