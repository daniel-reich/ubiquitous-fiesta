
def climb(stamina, obstacles):
  now=obstacles[0]
  for i in range(1,len(obstacles)):
    trg,mem=obstacles[i],0
    if trg>now:mem=2*(((trg-now)//1)+(((trg-now)%1)!=0))
    if trg<now:mem=((now-trg)//1)+((now-trg)%1!=0)
    if stamina-mem<0:i-=1;break
    else:stamina,now=stamina-mem,trg
  return i

