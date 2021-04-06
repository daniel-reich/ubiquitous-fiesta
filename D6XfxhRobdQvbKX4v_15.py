
def first_before_second(s, first, second):
  true = True
  firstIndexes = [i for i, j in enumerate(s) if j == first]
  secondIndexes = [i for i, j in enumerate(s) if j == second]
  for fIndex in firstIndexes:
    for sIndex in secondIndexes:
      if fIndex > sIndex:
        true = False
      else:
        pass
  return true

