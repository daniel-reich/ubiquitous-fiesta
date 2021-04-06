
def chi_squared_test(data):
#sum of table
  two_hours = data["E"][0] + data["T"][0]
  half_hours = data["E"][1] + data["T"][1]
  EDA = data["E"][0] + data["E"][1]
  TUT = data["T"][0] + data["T"][1]
  total = two_hours + half_hours
  #transformed table
  tbl1 = ((data["E"][0] - two_hours*EDA/total)**2)/(two_hours*EDA/total)
  tbl2 = ((data["E"][1] - EDA*half_hours/total)**2)/(EDA*half_hours/total)
  tbl3 = ((data["T"][0] - TUT*two_hours/total)**2)/(TUT*two_hours/total)
  tbl4 = ((data["T"][1] - half_hours*TUT/total)**2)/(half_hours*TUT/total)
  chi = round((tbl1+tbl2+tbl3+tbl4),1)
  if chi > 6.635:
    return [chi,"Edabitin effectiveness = 99%"]
  elif chi > 3.841 and chi < 6.635:
    return [chi,"Edabitin effectiveness = 95%"]
  else:
    return [chi,"Edabitin is ininfluent"]

