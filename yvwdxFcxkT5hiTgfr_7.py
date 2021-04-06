
def get_xp(d):
  dic={
  'Very Easy': 5,
  'Easy': 10,
  'Medium':20,
  'Hard':40,
  'Very Hard':80}
  index=['Very Easy','Easy','Medium','Hard','Very Hard']
  pt=0
  for i in index:
    pt+=d[i]*dic[i]
  return str(pt)+'XP'

