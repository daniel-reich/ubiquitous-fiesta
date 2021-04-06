
def free_throws(success, rows):
  suc = success.split('%')
  dec = int(suc[0])
  dec = float(dec)/100
  return str(round((dec ** rows) * 100)) + '%'

