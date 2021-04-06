
def greatest_impact(lst):
  # lst in format: [Mood, Weather, Meals, Sleep]
  factor_list = []
  elm         = 0 
  for x in range (4):
    for y in range (len (lst)):
      elm += int (lst[y][x])
    if x == 2:
      elm*= 10/3
    factor_list.append (elm)
    elm = 0 
  factor_list = factor_list[1:]
  avg = sum (factor_list)//3
  print ('A',avg)
  highest_diff = abs (factor_list[0] - avg)
​
  same_num = 0 
  for i in factor_list:
    print ('highest_diff:',highest_diff)
    if highest_diff == abs(i-avg):
      print ('Abs',abs (i-avg))
      same_num += 1
    if abs (i - avg) > highest_diff:
      highest_diff = abs (i-avg)
  
  print(factor_list)  
  print ( highest_diff)
  print (same_num)
  
  try:
    index = factor_list.index(highest_diff+avg)
    
  except:
    index = factor_list.index(abs(highest_diff-avg))
  print (index)
  if same_num != 3: 
    if index == 0:
      return 'Weather'
    elif index == 1:
      return 'Meals'
    elif index == 2:
      return 'Sleep'
  else:
    return 'Nothing'

