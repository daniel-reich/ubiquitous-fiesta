
def get_best_student(grades):
  avgs = []
  for st in grades:
    av = sum(grades[st])/len(grades[st])
    avgs.append((av, st))
  avgs.sort(reverse=True)
  return avgs[0][1]

