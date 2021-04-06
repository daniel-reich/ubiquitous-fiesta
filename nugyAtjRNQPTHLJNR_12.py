
def pages_in_book(total):
  n = int(((1+8*total)**0.5-1)/2)
  return n*(n+1)//2 == total

