
def get_best_student(grades):
  ret = sorted(grades.items(), key=lambda x: -sum(x[1])/len(x[1])) 
  return ret[0][0]

