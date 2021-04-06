
def free_throws(success, rows):
  a = (int(success[:-1]) * 0.01) ** rows 
  return str(round(a*100)) + "%"

