
def pages_in_book(total):
  for i in range(1,10000000000000000000000000000):
    if i*(i+1)>=2*total:
      return i*(i+1)==2*total

