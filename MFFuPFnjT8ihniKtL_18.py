
def bug_jump(height, time):
  h=height- (time/1000 - height**(0.5) )**2
  diff= - 2 * (time/1000 - height**(0.5) )
  
  if h<0 : return [0, None]
  
  if diff>0 : r= "up" 
  if diff<0 : r= "down"
  
  return [round(h,2),r]

