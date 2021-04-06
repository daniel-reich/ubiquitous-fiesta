
def over_time(lst):
  print(lst)
  # calc overtime:
  out =max(min(9,lst[1])-lst[0],0)
  out+=max(lst[1]-max(17,lst[0]),0) 
  print(out)
  out=out*(lst[3]-1) + lst[1]-lst[0] # overtime* (multiplier-1) + workinghours
  
  return("$"+'{0:.2f}'.format(round(out*lst[2]+0.001,2)) )

