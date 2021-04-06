
def dice_game(lst):
  t=0
  for x in lst:
   if x[0]==x[1]:
          t=0;break
        
   s=x[0]+x[1]
   t+=s
  
  return t

