
def free_throws(success, rows):
  return '{:.0%}'.format((int(success[0:2])/100)**rows)

