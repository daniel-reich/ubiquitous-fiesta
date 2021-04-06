
def percentage_changed(old, new):
  new_old = int(old[1:])
  new_new = int(new[1:])
  result = ""
  percent = round((new_new / new_old) * 100)
  if new_old > new_new:
    result = str(abs(100-percent))+"%"+" "+"decrease"
  elif new_old < new_new:
    result = str(abs(100-percent))+"%"+" "+"increase"
  return result

