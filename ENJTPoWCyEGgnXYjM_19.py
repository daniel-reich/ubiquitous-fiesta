
def percent_filled(box):
  x = [sum(x.count('o') for x in box), sum(x.count(' ') for x in box)]
  return str(int(x[0]/(x[1] + x[0])*100)) + '%'

