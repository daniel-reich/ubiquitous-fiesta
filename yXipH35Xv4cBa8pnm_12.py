
def microwave_buttons(time):
  a=int(time[:2])
  b=int(time[-2:])
  if a==0:
    if b==0:return 1
    elif b==30:return 2
    else:return 3
  if a==1:return 3
  if a==10:return 5

