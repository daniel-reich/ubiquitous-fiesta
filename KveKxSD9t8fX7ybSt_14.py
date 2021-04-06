
def final_countdown(lst):
  lst=lst[::-1]
  combos=[]
  for i in range(len(lst)):
    if lst[i]==1:
      combos.append(check(lst[i:]))
  return [lst.count(1),combos[::-1]]
      
      
​
def check(lst):
  print("in check:",lst)
  b=[]
  for i,e in enumerate(lst):
    if i+1 ==e :
      b.append(e)
    else:
      break
  return b[::-1]

