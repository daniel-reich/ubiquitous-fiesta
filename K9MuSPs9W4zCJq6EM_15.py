
def cycle_length(lst, n):
  count= 0
  while True:
    
    if n == lst[n-1]:
      print (count)
      exit()
    nindex = lst.index(n) # index number of n (2)
    lst[nindex] = n-1 # put corresponding number at index number of n (index psn 2)
    lst[n-1] = n # put n at the index psn of where the cooresponding number came from
    count = count + 1
    
    print(lst)

