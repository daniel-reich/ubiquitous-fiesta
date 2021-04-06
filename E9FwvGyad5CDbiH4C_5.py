
def block(lst):
  people = 0
  for idx, row in enumerate(lst):
    for col in row:
      if col == 2:
        people  += len(lst) - (idx + 1)
  return people

