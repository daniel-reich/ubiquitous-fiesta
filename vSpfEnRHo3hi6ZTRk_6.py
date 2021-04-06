
def free_throws(success, rows):
  perc = int(success.replace('%', '')) / 100
  return str(int(round(perc ** rows * 100, 0))) + '%'

