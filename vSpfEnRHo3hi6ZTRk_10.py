
def free_throws(success, rows):
  return str(int(round((int(success[:2])/100)**rows, 2)*100))+"%"

