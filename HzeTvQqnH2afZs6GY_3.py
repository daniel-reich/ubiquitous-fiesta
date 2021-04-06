
def generate_rug(n, direction):
  rug=[]
  for i in range(n):
    rugrow = []
    for j in range(n-i):
      rugrow.append(n-i-j-1)
    for j in range(i):
      rugrow.append(j+1)
    if(direction == "left"):
      rugrow = rugrow[::-1]
    rug.append(rugrow)
  return(rug)

