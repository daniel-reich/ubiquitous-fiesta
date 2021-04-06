
def pages_in_book(total):
  i=1
  sum=0
  while sum!=total :
    if sum < total:
      sum=sum+i
      i+=1
    else:
      return False
      break
  return True

