
def get_xp(d):
  points = [
    d.get('Very Easy') * 5,
    d.get('Easy') * 10,
    d.get('Medium') * 20,
    d.get('Hard') * 40,
    d.get('Very Hard') * 80
  ]
  return '{}XP'.format(sum(points))

