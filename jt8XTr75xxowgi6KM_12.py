
def get_student_top_notes(students):
  l=[]
  for i in students:
    if i['notes']==[]:
      l.append(0)
    else:
      l.append(max(i['notes']))
  return l

