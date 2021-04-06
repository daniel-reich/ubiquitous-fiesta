
from collections import Counter
def get_notes_distribution(students):
  print(students)
  students_list_of_lists = [s['notes'] for s in students]
  res = dict(Counter([item for sublist in students_list_of_lists\
  for item in sublist if item in [1,2,3,4,5]]))
  return res

