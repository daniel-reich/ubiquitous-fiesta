
def get_student_top_notes(students):
  return [max(stud["notes"], default=0) for stud in students]

