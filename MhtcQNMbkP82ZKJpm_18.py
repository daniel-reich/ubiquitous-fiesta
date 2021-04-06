
def get_notes_distribution(students):
  new_list = []
  for i in students:
    new_list.append(i["notes"])
  together = []
  valid = [1, 2, 3, 4, 5]
  for i in new_list:
    for x in i:
      if x in valid:
        together.append(x)
  uniq = []
  for i in together:
    if i not in uniq:
      uniq.append(i)
  distribution = {}
  for i in uniq:
    distribution[i] = together.count(i)
  return distribution

