
def scale_tip(lst):
  a,b,c=[0,0,0]
  for i in range(0, len(lst)):
      if c==0:
          if lst[i] == 'I':
              c+=1
          else:
              a+=lst[i]
      else:
          b+=lst[i]
  return 'left' if a>b else 'right' if b>a else 'balanced'

