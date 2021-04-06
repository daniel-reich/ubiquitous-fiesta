
def back_to_home(directions):
  direct_n = directions.count("N")
  direct_e = directions.count("E")
  direct_w = directions.count("W")
  direct_s = directions.count("S")
  if direct_s == direct_n and direct_e == direct_w :
    return True
  else:
    return False

