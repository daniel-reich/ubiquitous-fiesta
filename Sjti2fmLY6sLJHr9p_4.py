
def look_and_say (start,n):
  lst = []
  num = start
  for i in range (n):
    lst.append (num)
    num_lst = []
    if len (str (num)) == 1:
      num_lst.append (1) 
      num_lst.append (num)
    else:
      num_num =1
​
      for x in range (len (str(num))-1):
        if str (num)[x+1] == str (num)[x]:
          num_num +=1
        else:
           num_lst.append (num_num)
           num_lst.append (int(str(num)[x]))
           num_num = 1 
      num_lst.append (num_num)
      num_lst.append (int(str(num)[x+1]))
    num = 0 
    print ('num_lst:',num_lst)
    for z in range (len(num_lst)):
      num+= num_lst[z]*10**(len (num_lst)-z-1)
      print ('Index',z)
​
​
    print ('Num:',num)
  return lst

