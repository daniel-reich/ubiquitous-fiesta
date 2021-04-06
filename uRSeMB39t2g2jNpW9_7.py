
def turn_calc(num):
  return str(num)[::-1].replace(".","").translate(str.maketrans("012345678","OIZEHSGLB"))

