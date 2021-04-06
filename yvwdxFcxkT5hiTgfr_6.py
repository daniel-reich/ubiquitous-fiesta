
def get_xp(d):
  xp = [5, 10, 20, 40, 80]
  xp2 = 'Very Easy', 'Easy', 'Medium', 'Hard', 'Very Hard'
  return str(sum([i*d[j] for i,j in zip(xp, xp2)])) + 'XP'

