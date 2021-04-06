
def free_throws(success, rows):
  return str(round(((float(success[:-1]) / 100) ** rows) * 100)) + "%"

