
def seesaw(num):
  num = str(num)
  if len(num) > 1 and num != 'None':
    l = int(num[:len(num)//2])
    r = int(num[(len(num)//2):]) if not len(num)%2 else int(num[1 + (len(num)//2):])
    return 'left' if l > r else 'right' if r > l else 'balanced'
  return 'balanced'

