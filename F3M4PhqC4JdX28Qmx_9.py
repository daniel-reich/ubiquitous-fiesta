
def back_to_home(directions):
  if directions.count('N') == directions.count('S') and directions.count('W') == directions.count('E'):
    return True
  else:
    return False

