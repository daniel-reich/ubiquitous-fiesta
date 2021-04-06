
def get_best_student(grades):
  dic,avg={},[]
  for key,value in grades.items():
    out = float(sum(value)/len(value))
    dic.update({key:out})
    avg.append(out)
  for key,value in dic.items():
    if value == max(avg):
      return key

