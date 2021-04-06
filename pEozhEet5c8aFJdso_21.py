
def all_about_strings(txt):
  if len(txt) % 2 == 0:
    middle1 = int(len(txt) / 2 - 1)
    middle2 = int(middle1 + 2)
  else:
    middle1 = int(len(txt) / 2)
    middle2 = int(middle1 + 1)
  index = txt.find(txt[1],2)
  if index != -1:
    index = "@ index " + str(index)
  else:
    index = "not found"
  return [len(txt), txt[0], txt[-1], txt[middle1:middle2], index]

