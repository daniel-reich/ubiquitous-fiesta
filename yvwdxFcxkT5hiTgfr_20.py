
def get_xp(d):
  l = []
  l.append(d.get("Very Easy")*5)
  l.append(d.get("Easy")*10)
  l.append(d.get("Medium")*20)
  l.append(d.get("Hard")*40)
  l.append(d.get("Very Hard")*80)
  return str(sum(l)) + "XP"

