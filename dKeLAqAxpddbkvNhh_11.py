
def group_seats(lst, n):
  spots=0
  for row in lst:
    count=0
    for elem in row:
      if(elem==0):
        count+=1
      else:
        count=0
      if(count==n or count>=n):
        spots+=1
  return(spots)

