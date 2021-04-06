
def fibo_word(n):
  if n < 2:
    return 'invalid'
  mylist = ['b','a']
  for i in range(n-2):
    mylist.append(mylist[-1]+mylist[-2])
    
  myans = 'b'
  for i in range(1,n):
    myans += ', ' + mylist[i]
  return myans

