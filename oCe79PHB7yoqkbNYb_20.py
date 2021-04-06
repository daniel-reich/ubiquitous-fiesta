
def break_point(num):
  
  num_arr = [int(x) for x in str(num)]
  sum_L = 0
  sum_R = 0
  
  for i in range(len(num_arr)):
    sum_L = sum(num_arr[:i+1])
    sum_R = sum(num_arr[i+1:len(num_arr)])
    
    if (sum_L == sum_R):
      return True
  return False

