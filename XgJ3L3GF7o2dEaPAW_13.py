
def shared_letters(a, b):
​
  result_str = ""
  result = ""
  
  for char in a.lower():
    if char in  b.lower():
      if char not in result_str:
        result_str += char
  
  for i in sorted(result_str):
    result += i
      
  return result

