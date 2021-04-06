
def snakefill(n):
  bo_area ,sn_area=n**2 , 1
  steps =0
  while True :
    if sn_area < bo_area:
      sn_area*=2
      steps+=1
    else : 
      if sn_area != bo_area:
        steps-=1
      break
  return steps

