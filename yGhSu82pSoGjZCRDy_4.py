
def seesaw(num):
  snum = str(num)
  if num == None or len(snum)==1:
    return 'balanced'
  if len(snum)%2==0:
    i = int(len(snum)/2)
    left = int(snum[:i])
    right = int(snum[i:])
  else:
    i = int(len(snum)//2)
    left = int(snum[:i])
    right = int(snum[i+1:])
  if left > right:
    return 'left'
  elif right > left:
    return 'right'
  else:
    return 'balanced'

