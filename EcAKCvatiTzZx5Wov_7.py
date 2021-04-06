
def string(n: float):
  if int(n) == n:
    return str(int(n))
  else:
    return str(n)
​
def resistor_code(col: list):
​
  dm_code = {
      "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
      "blue": 6, "violet": 7, "gray": 8, "white": 9, "gold": -1, "silver": -2
  }
  tl_code = {
      "brown": '1', "red": '2', "green": '0.5', "blue": '0.25', "violet": '0.1', 
      "gray": '0.05', "gold": '5', "silver": '10'
  }
  tcr_code = {
      "brown": '100', "red": '50', "orange": '15', "yellow": '25', "blue": '10', 
      "violet": '5'
  }
  if len(col) == 4:
    resistance = (dm_code[col[0]] * 10 + dm_code[col[1]]) * 10 ** dm_code[col[2]]
    tolerance = " +/-" + tl_code[col[3]] + "%" 
  else:
    resistance = (dm_code[col[0]] * 100 + dm_code[col[1]] * 10 + dm_code[col[2]]) * 10 ** dm_code[col[3]]
    tolerance = " +/-" + tl_code[col[4]] + "%" 
  if resistance // 10 ** 9:
    resistance = string(resistance / 10 ** 9) + "GOhm"
  elif resistance // 10 ** 6:
    resistance = string(resistance / (10 ** 6)) + "MOhm"
  elif resistance // 10 ** 3:
    resistance = string(resistance / 10 ** 3) + "kOhm"
  else:
    resistance = string(resistance) + "Ohm"
  
  if len(col) == 6:
    tcr = " " + tcr_code[col[5]] + "ppm/k"
  else:
    tcr = ""
​
  return resistance + tolerance + tcr

