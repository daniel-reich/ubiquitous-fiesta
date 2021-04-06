
def seesaw(num):
  if len(str(num)) < 2 or num == None:
    return "balanced"
  txt = ""
  if len(str(num)) % 2 == 1:
    lst = list(str(num))
    lst.pop(int(len(str(num))/2 -0.5))
    for i in lst:
      txt += i
  else:
    txt = str(num)
​
  h = int(len(txt)/2) 
  left = int(txt[:h])
  right = int(txt[h:])
​
  if left > right: return "left"
  elif left < right: return "right"
  else: return "balanced"

