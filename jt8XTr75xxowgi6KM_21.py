
def get_student_top_notes(students):
  topnotes = []
  for i in students:
    try:
      topnotes.append(max(i['notes']))
    except:
      topnotes.append(0)
  return topnotes

