
MAX = 10000
arr = []   
def ulam(n): 
  s = set()  
  arr.append(1)  
  s.add(1)  
  arr.append(2)  
  s.add(2)  
  for i in range(3, MAX):  
    count = 0
    for j in range(0, len(arr)):  
      if (i - arr[j]) in s and arr[j] != (i - arr[j]):  
        count += 1
      if count > 2:  
        break
    if count == 2: 
      arr.append(i)  
      s.add(i)  
  return arr[n-1]

