
def arithmetic_progression(start, diff, n):
  lst0 =[]
  c = 0
  s = ""
  lst =[start]
  result = start
  for i in range(n - 1):
    result += diff
    lst.append(result)
  s1 = str(lst)
  
  for letter in s1:
    if letter != '[' and letter != ']':
      s += letter
    
  return s

