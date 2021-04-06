
def free_throws(success, rows):
  success = int(success.strip('%')) / 100
  result = str(round(success ** rows * 100)) + '%'
  return result

