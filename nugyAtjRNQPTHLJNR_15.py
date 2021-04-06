
def pages_in_book(total):
  d = 0
  for i in range(1, total+1):
    d+=i
    if total == d:
      return True
  else:
    return False

