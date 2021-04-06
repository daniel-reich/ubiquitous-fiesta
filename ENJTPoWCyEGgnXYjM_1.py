
def percent_filled(box):
  empty = sum(sum(1 for j in i if j is ' ') for i in box)
  filled = sum(sum(1 for j in i if j is 'o') for i in box)
  return '{}%'.format(round(filled/(filled+empty)*100))

