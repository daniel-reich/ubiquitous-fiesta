
def ascending(txt):
  print(txt)
  for i in range(1,len(txt)//2+1):
    temp = []
    for x in range(0,len(txt),i):
      temp.append(int(txt[x:x+i]))
    print(temp)
    if check(temp):
      return True
  return False
​
def check(lst):
  for i in range(1,len(lst)):
    if lst[i] != lst[i-1]+1:
      return False
  return True

