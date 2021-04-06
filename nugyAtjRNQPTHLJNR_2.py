
def pages_in_book(total):
​
  pages_sum = 0
  pages = 0
  
  while pages_sum < total:
    pages_sum += pages
    pages += 1
    
  if pages_sum == total:
    return True
  else:
    return False

