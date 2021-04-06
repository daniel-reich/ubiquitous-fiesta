
def pages_in_book(total):
  if total:
    sum = 0 
    for i in range(1, total):
      sum += i
      if (sum == total):
        return True
      elif (sum > total):
        return False
  else:
    return False

