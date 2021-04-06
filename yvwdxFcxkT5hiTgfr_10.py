
def get_xp(d):
  dictionary = {"Very Easy" : 5, "Easy" : 10, "Medium" : 20, "Hard" : 40, "Very Hard" : 80}
  return "{}XP".format(sum(dictionary[m]*n for m,n in zip(d.keys(),d.values())))

