
def power_ranger(power, minimum, maximum):
  count = 0
  
  for i in range(round(minimum**(1/power)), round(maximum**(1/power))+1):
    count += 1
    
  return count
  
  
  
# power_ranger(2, 49, 65) => 2
# 2 squares (n^2) lie between 48 and 65, 49 (7^2) and 64 (8^2)

