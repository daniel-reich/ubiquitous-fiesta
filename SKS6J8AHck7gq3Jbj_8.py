
def tidy_books(lst):
  for i in range(len(lst)):
    temp=lst[i][0].split(' - ')
    temp[0]=temp[0].lstrip()
    temp[1]=temp[1].rstrip()
    lst[i]=temp
  return lst

