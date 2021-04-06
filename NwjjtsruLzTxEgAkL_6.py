
def assignment(date):
  date = date.split('/')
  if len(date[0]) != 4:
    return False
  else:
    if int(date[1]) >= 13 or len(date[1]) < 2:
      return False
    else:
      return True

