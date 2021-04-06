
def get_best_student(dic):
  return sorted([k for k in dic.keys()], key = lambda k: sum(dic[k])/3)[-1]

