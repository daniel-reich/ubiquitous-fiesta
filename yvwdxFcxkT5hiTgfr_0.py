
def get_xp(d):
  v = {'Very Easy':5,'Easy':10,'Medium':20,'Hard':40,'Very Hard':80}
  return '{}XP'.format(sum({d[i]*v[i] for i in d.keys()}))

