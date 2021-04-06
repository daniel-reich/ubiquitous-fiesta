
def pages_in_book(total):
  x = 0
  for i in range(total):
    x += i
    if x == total:
      return True
  return False

