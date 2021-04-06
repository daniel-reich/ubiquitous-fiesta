
def avg_note(students):
  for student in students:
    student['avgNote'] = round(average(student['notes']))
    del student['notes']
  return students
  
def average(lst):
  return sum(lst) / len(lst) if lst else 0

