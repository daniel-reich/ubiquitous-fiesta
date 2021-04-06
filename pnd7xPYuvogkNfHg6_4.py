
def get_best_student(grades):
  new_dict = {}
  for key in grades:
    new_dict[key] = round(sum(grades[key]) / len(grades[key]), 2)
  return max(new_dict, key = new_dict.get)

