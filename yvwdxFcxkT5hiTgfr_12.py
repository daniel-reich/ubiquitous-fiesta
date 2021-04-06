
def get_xp(d):
  sum=d['Very Easy']*5 + d["Easy"]*10
  sum=sum + d["Medium"]*20 + d["Hard"]*40
  sum = sum + d["Very Hard"]*80
  return str(sum)+"XP"

