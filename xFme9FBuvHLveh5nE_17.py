
def is_zygodrome(num):
  num = str(num)
  list_num_place = 0
  list_num = [[num[list_num_place]]]
  actual_value = num[0]
  score = 0
  
  for s in range(1, len(num)):
    if num[s] == actual_value:
      list_num[list_num_place].append(num[s])
      actual_value = num[s]
    else:
      list_num_place += 1
      list_num.append([])
      list_num[list_num_place].append(num[s])
      actual_value = num[s]
      
  score = sum([1 for nl in list_num if len(nl) > 1])
      
  return score == len(list_num)

