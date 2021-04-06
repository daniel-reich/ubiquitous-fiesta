
def seq_level(lst):
  lvl=0
  while True:
    lvl+=1
    runLst=[]
    for i in range(1,len(lst)):
      runLst.append(lst[i]-lst[i-1])
    if len(set(runLst))==1: break
    lst=runLst[:]
  if lvl==1: return 'Linear'
  if lvl==2: return 'Quadratic'
  if lvl==3: return 'Cubic'

