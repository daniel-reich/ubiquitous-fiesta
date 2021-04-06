
def dice_score(throw):
  
  d={1:{1:100,3:1000},5:{1:50,3:500},2:{3:200},3:{3:300},4:{3:400},6:{3:600}}
  
  return sum(d[s].get(throw.count(s),0) for s in set(throw))

