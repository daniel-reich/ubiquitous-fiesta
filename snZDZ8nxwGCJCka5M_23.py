
import math
def isTriangular(num): 
  
    if (num < 0): 
        return False
        
    c = (-2 * num) 
    b, a = 1, 1
    d = (b * b) - (4 * a * c) 
  
    if (d < 0): 
        return False
  
    root1 = ( -b + math.sqrt(d)) / (2 * a) 
    root2 = ( -b - math.sqrt(d)) / (2 * a) 
  
    if (root1 > 0 and math.floor(root1) == root1): 
        return True
  
    if (root2 > 0 and math.floor(root2) == root2): 
        return True
  
    return False
​
def pyramidal_string(string, _type):
  if not string:
    return []
  if isTriangular(len(string)):
    if _type == "REG":
      ans = []
      n = 1
      while string:
        a = string[:n]
        b = [let+' ' for let in a[:-1]]
        b.append(a[-1])
        ans.append(''.join(b))
        string = string[n:]
        n += 1
      return ans
    if _type == "REV":
      ans = []
      n = 1
      while string:
        a = string[-n:]
        b = [let+' ' for let in a[:-1]]
        b.append(a[-1])
        ans.append(''.join(b))
        string = string[:-n]
        n += 1
      ans.reverse()
      print(ans)
      return ans
  else:
    return 'Error!'

