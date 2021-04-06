
def over_time(lst):
  earn = (lst[1]-lst[0])*lst[2]
  if lst[0]>=17: earn*=lst[3]
  elif lst[1]>17: earn+=(lst[1]-17)*(lst[3]-1)*lst[2]
  tot=str(round(earn*100+10**(-10)))
  return '$'+tot[:-2]+'.'+tot[-2:]

