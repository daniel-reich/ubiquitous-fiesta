
def get_xp(d):
  total = d['Very Easy'] * 5 + d['Easy'] * 10 + d['Medium'] * 20 + d['Hard'] * 40 + d['Very Hard'] * 80
  
  return str(total) + "XP"

