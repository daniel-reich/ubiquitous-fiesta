
def sock_merchant(lst):
  
  Original = lst
​
  Unique = set(Original)
  Unique = list(Unique)
​
  Events = []
  
  for x in Unique:
    Events.append(Original.count(x))
    
  Total = 0
    
  for x in Events:
    Total += (x//2)
    
  return Total

