
def pages_in_book(total):
  a=0
  for i in range(total):
    a+=i
    if a==total:return True
    if a>total:return False

