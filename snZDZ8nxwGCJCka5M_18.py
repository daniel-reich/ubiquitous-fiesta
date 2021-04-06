
import math
​
def equation(n):
  return ((n+1)*(n)) // 2
​
def equation2(n,k):
  return (n*k) - equation(k)
​
def join_strings(letters):
  if len(letters) > 1:
    k = [char + " " for char in letters[:-1]]
    join = ''.join(k)
    return join + letters[-1]
  else:
    return letters
​
def pyramidal_string(string, _type):
  if string == "":
    return []
  elif len(string) == 1:
    return [string]
  n = (1+math.sqrt(1+(8*len(string))))/ 2
  if (n).is_integer():
    n = int(n)
    lst = []
    if _type == "REG":
      for i in range(0,n):
        lst.append(string[equation(i):equation(i+1)])
    else:
      for i in range(0,n):
        lst.append(string[equation2(n,i):equation2(n,i+1)])
    lst = list(map(lambda x: join_strings(x),lst))
    
    lst.remove("")
    return lst
    
        
      
    
  else:
    return "Error!"

