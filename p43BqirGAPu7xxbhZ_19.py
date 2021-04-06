
def diamond(carat):
  lst = [[0 for i in range(carat)] for i in range(carat if carat%2==1 else carat-1)]
  a = (carat-1)//2 
  for i in range((carat+1)//2):     
    lst[a][i],lst[a][-(i+1)],lst[-(a+1)][i],lst[-(a+1)][-(i+1)] = 1,1,1,1
    a -= 1
  return [lst,('good cut' if carat%2==0 else 'perfect cut')]

