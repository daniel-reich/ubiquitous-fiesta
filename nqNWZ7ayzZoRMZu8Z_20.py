
def avg_note(students):
  result = []
  for student in students:
    if student["notes"] == []:
      result.append({"name":student["name"], "avgNote":0})
      continue
    average = 0
    for score in student["notes"]:
      average += score
    average /= len(student["notes"])
    average = round(average)
    result.append({"name":student["name"], "avgNote":average})
  return result

