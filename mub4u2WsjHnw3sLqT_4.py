
def lambda_depth(num=0):
  if num > 0:
    lambda_depth.n = 0
    lambda_depth.g = num
​
  if lambda_depth.n == lambda_depth.g:
    lambda_depth.n = 0
    return "edabit"
  else : 
    lambda_depth.n += 1
    return lambda_depth
    
lambda_depth.n = 0
lambda_depth.g = 0

