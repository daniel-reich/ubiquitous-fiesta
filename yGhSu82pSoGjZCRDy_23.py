
def seesaw(num):
  if not num or len(str(num))==1:
    return 'balanced'
  left = str(num)[:len(str(num))//2]
  right = str(num)[len(str(num))//2:]
  right = right[len(right)-len(left):]
  return 'right' if int(right)>int(left) else 'left' if int(right)<int(left) else 'balanced'

