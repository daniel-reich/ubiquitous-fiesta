
def result_parsing(s):
  s1=s.replace(' ','')
  s2=s1.split('-')
  return (s2[0][0],int(s2[0][1:]),s2[1][-1],int(s2[1][0:-1]))
tn={'A':0, 'B':1, 'C':2, 'D':3}
tnr={'0':'A', '1':'B', '2':'C', '3':'D'}
def tournament_scores(rl):
  #(Team1,sg,Team2,sg)
  rl1=list(map(result_parsing,rl))
  print(rl1)
  #Team, win, loss, tie, sg, cg
  stat=[[tnr[str(n)],0,0,0,0,0] for n in range(len(tnr))]
  for x in rl1:
    stat[tn[x[0]]][4]+=x[1]
    stat[tn[x[0]]][5]+=x[3]
    stat[tn[x[2]]][4]+=x[3]
    stat[tn[x[2]]][5]+=x[1]
    if x[1] > x[3]:
      stat[tn[x[0]]][1]+=1
      stat[tn[x[2]]][2]+=1
    elif x[1] < x[3]:
      stat[tn[x[0]]][2]+=1
      stat[tn[x[2]]][1]+=1
    else:
      stat[tn[x[0]]][3]+=1
      stat[tn[x[2]]][3]+=1
  print(stat)
  #Team, pt, gs gd
  result=[[tnr[str(n)], stat[n][1]*3+stat[n][3], stat[n][4], stat[n][4]-stat[n][5]] for n in range(len(tnr))]
  result_sorted1=list(sorted(result, key=lambda x: x[3], reverse=True))
  result_sorted2=list(sorted(result_sorted1, key=lambda x: x[2], reverse=True))
  result_sorted3=list(sorted(result_sorted2, key=lambda x: x[1], reverse=True))
  return result_sorted3

