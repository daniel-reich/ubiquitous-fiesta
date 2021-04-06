
def get_notes_distribution(students):
  x = {}
  a = []
  for i in students:
    for k in i["notes"]:
      if 0<k<6:
        a.append(k)
  p = sorted(set(a), reverse=True)
​
  for i in p:
    x.update({i:a.count(i)})
​
  return x

