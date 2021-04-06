
def get_best_student(grades):
  result = 0
  final = ''
  for name, lst in grades.items():
    if (sum(lst) / len(lst)) > result:
      result = (sum(lst) / len(lst))
      final = name
  return final

