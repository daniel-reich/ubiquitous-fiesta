
def is_valid_date(d, m, y):
  months31 = (1, 3, 5, 7, 8, 10, 12)
  months30 = (4, 6, 9, 11)
  if int(d)<33:
    if m == 2 and int(d) < 29:
      return(True)
    for x in months31:
      if int(m) == int(x) and int(d) < 32:
        return(True)
    for x in months30:
      if int(m) == int(x) and int(d) < 31:
        return(True)
  return(False)

