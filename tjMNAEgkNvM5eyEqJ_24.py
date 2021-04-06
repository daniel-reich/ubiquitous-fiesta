
def unique_abbrev(abbs, words):
  required_count = len(abbs)
  count = 0
  for i in range(len(abbs)):
    x = abbs[i]
    y = len(x)
    for eachword in words:
      if x in eachword[0:y]:
        count += 1
  return required_count == count

