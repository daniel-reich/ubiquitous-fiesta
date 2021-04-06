
def swap_cards(n1, n2):
  low=min([int(i) for i in str(n1)])
  opp=str(low)+str(n2)[1]
  paul=[str(n1)[0],str(n1)[1]]
  paul.remove(str(low))
  paul.append(str(n2)[0])
  
  pscore=''
  if paul[0]==str(n1)[0]:
    pscore=paul[0]+paul[1]
  else:
    pscore=paul[1]+paul[0]
    
  if str(n1)[0]==str(n1)[1]:
    pscore=int(str(pscore)[::-1])
    return int(pscore)>int(opp)
  else:
    return int(pscore)>int(opp)

