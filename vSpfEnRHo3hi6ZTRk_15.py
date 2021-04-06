
def free_throws(success, rows):
  return str(round((int(success[:-1])/100)**int(rows)*100)) + '%'

