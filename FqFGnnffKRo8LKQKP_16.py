
def simple_numbers(a, b):
  ans = []
  
  for num in range(a, b+1):
    if sum(int(val)**(i+1) for i,val in enumerate(str(num))) == num:
      ans.append(num)
    
  return ans

