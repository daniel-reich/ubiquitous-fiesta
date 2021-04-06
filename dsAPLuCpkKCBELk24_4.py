
def multiply(arr):
  result = 1
  for x in arr:
    result*=x
  return result 
  
def get_products(lst):
  arr = [] 
  for i in range(0, len(lst)):
    arr.append(lst[:i] + lst[i+1:])
  return [multiply(x) for x in arr]

