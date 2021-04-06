
def consecutive(numbers):
  if len(numbers) < 2:
    return False
  for i in range(0,len(numbers)-1):
    if (numbers[i+1] - numbers[i]) != 1:
      return False
  return True
​
def splitByNumDigits(inputstr,num):
  arr = []
  remainder = len(inputstr) % num
  iseven = remainder == 0
  if not iseven: 
    arr.append(int(inputstr[0:remainder]))
  for i in range(remainder,len(inputstr),num):
    arr.append(int(inputstr[i:i+num]))
  #print(arr)
  return arr
  
def ascending(txt):
  midpoint = len(txt) // 2
  for i in range(1,midpoint+1):
    arr = splitByNumDigits(txt,i)
    if consecutive(arr) == True:
      return True
  return False

