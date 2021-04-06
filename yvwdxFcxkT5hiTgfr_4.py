
def get_xp(d):
  dic = {'Very Easy': 5, 'Easy':  10, 'Medium': 20, 'Hard': 40, 'Very Hard':  80}
  return str(sum(dic[nome] * d[nome] for nome in dic))+'XP'

