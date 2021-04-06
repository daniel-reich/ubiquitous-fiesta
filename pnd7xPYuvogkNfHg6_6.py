
def get_best_student(grades):  
  max = 0
  for x in grades.keys():
    if sum(grades[x]) / len(grades) > max:
     max += sum(grades[x]) / len(grades)
     stud = x
  return(stud)

