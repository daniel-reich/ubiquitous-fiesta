
def get_notes_distribution(students):
  d, arr = dict(), []
  for x in students:
    for n in x["notes"]:
      if n in [1,2,3,4,5]:
        arr.append(n)
  for z in set(arr):
    d[z] = arr.count(z)
  return d

