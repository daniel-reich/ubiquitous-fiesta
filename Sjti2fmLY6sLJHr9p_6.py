
def look_and_say(start, n):
  occur = []
  occur.append(start)
​
  while n > 1:
    lst = []
    current = str(start)[0] 
    new = str(start)[0] 
​
​
    for i in str(start)[1:] + " ":
      if i != current:
        
        lst.append(new)
        new = i
        current = i
        
      else:
        new += i 
      
​
    lst = [str(len(i)) + i[0] for i in lst]
    start = int("".join(lst))
    occur.append(start)
    n-=1
  
  return occur

