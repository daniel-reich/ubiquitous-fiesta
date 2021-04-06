
def compress(lst):
  res = "" 
​
  temp_lst = [] 
  counter = 0 
​
​
  for i in range(len(lst)):
​
    if not temp_lst:
      temp_lst.append(lst[0]) 
      counter += 1 
​
    else:
      next_ele = lst[i] 
​
      if temp_lst[-1] == next_ele:
        counter += 1 
​
      if temp_lst[-1] != next_ele:
        if counter == 1:
          pass
        else:
          temp_lst.append(str(counter)) 
​
        counter = 1
        temp_lst.append(lst[i]) 
​
      if i == len(lst) - 1:
        temp_lst.append(str(counter)) 
​
  return ("".join(temp_lst))

