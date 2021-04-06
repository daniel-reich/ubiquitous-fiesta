
def percent_filled(box):
  b="".join(x[1:-1] for x in box[1:-1])
  return "{}%".format(round(100*b.count("o")/len(b)))

