
def percent_filled(box):
  filled_space = sum([c == "o" for row in box for c in row])
  total_space = (len(box) - 2) * (len(box[0]) - 2)
  
  return "{}%".format(round(filled_space / total_space * 100))

