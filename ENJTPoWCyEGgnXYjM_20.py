
def percent_filled(box):
  filled, empty = 0, 0
  for item in box[1:-1]:
    for space in item[1:-1]:
      empty += 1
      if space == "o":
        filled += 1
  return "{}%".format(int(round((filled/empty) *100)))

