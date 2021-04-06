
def get_student_top_notes(students):
  lst=[]
  for i in students:
    try:
      lst+=[max(i["notes"])]
    except:
      lst+=[0]
  return lst

