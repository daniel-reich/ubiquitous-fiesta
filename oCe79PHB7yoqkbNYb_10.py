
def break_point(num):
  num_list = list(str(num))
  num_list = [int(i) for i in num_list]
  
  result = False
  for i in range(len(num_list)):
    if sum(num_list[:i]) == sum(num_list[i:]):
      result = True
  return result

