
def free_throws(success, rows):
  return str(round(((((int(success[:-1]))/100)** rows))*100)) + '%'

