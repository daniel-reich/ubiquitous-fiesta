
def pages_in_book(total):
  return total in [i*(i+1)/2 for i in range(int((total*2)**.6))]

