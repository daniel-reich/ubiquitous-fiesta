
def group_seats(lst, n):
 count=0
 #go through rows
 for i in range(0,len(lst)):
  # print('i',i)
  #find 0 in row i
  for k in range(0,len(lst[i])-n+1):
   # print('k',k)
   # print(lst[i][k])
   if lst[i][k] == 0:
   # if n-1 0's follow
    follow=True
    for p in range(1,n):
     # print('p',p)
     # print('lst[i][(k+p)]',lst[i][(k+p)])
     if lst[i][(k+p)] == 0:
      continue
     else:
      follow=False
      break
    # print('follow',follow)
    if follow:
     count+=1
    # print('count',count)
   
 return count

