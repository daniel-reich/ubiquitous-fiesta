
def microwave_buttons(time):
  left,right = time.split(':')
  thirty = -1
  if right in ('00','30'):
    thirty = int(left)*2 + (1 if right=='30' else 0)
  for i in left:
    if i=='0':
      left = left.replace('0','',1)
    else:
      break
  buttons = len(left)+len(right)
  return min(buttons,(thirty if thirty!=-1 else buttons))+1

