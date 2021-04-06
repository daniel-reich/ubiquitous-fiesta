
def seesaw(num):
​
  if len(str(num)) < 2 or num == None:
    return 'balanced'
​
  mid = len(str(num))//2
  left = int(str(num)[:mid])
​
  if len(str(num)) % 2 == 1:
    right = int(str(num)[mid+1:])
  else:
    right = int(str(num)[mid:])
  
  if left > right:
    return 'left'
  elif right > left:
    return 'right'
  else:
    return 'balanced'

