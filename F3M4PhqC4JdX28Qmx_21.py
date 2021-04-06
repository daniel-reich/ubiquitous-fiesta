
def back_to_home(directions):
  return True if directions.count("N") == directions.count("S") and directions.count("E") == directions.count("W") else False

