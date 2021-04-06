
def percent_filled(box):
  spaces = (len(box) - 2) * (len(box[0]) - 2)
  filling = ''.join(box).count('o')
  return str(round(filling/spaces*100)) + '%'

