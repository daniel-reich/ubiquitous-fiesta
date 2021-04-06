
def get_best_student(grades):
  return max(grades.keys(), key=lambda x:sum(grades[x])/len(grades[x]))

