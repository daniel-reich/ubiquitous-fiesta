
def percent_filled(box):
  return str(round((''.join(box).count('o') / ((len(box[0]) - 2) * (len(box) - 2))) * 100)) + '%'

