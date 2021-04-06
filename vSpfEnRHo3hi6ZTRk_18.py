
def free_throws(success, rows):
  p = float(success[:-1])/100
  return '{:.0%}'.format(p**rows)

