
def get_xp(d):
  e = {"Very Easy" : 5,
  "Easy" : 10,
  "Medium" : 20,
  "Hard" : 40,
  "Very Hard" : 80}
    
    
  return '{}XP'.format(sum({v * e[k] for k, v in d.items() if k in e}))

