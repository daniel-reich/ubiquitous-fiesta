
def hours_passed(time1, time2):
  if time1 == time2:
    return "no time passed"
  elif time1[-2:] == time2[-2:]:
    num1 = float(time1[:4].replace(":", "."))
    num2 = float(time2[:4].replace(":", "."))
    diff = int(num2 - num1)
    return str(diff) + " hours"
  else:
    num1 = float(time1[:4].replace(":", "."))
    num2 = float(time2[:4].replace(":", "."))
    diff = int((12.0-num1) + num2)
    return str(diff) + " hours"

