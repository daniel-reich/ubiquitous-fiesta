
def get_best_student(grades):
  lst = []
  for i in grades:
    lst.append([i, sum(grades[i]) / len(grades[i])])
  maxxx = [n[1] for n in lst]
  return lst[maxxx.index(max(maxxx))][0]

