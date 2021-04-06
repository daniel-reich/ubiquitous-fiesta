
def free_throws(success, rows):
  return '{:.0%}'.format(float('0.' + success[:-1])**rows)

