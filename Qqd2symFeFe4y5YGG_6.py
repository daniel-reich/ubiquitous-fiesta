
def palindromic_date(date):
  uk = "".join(date.split("/"))
  usa = "".join([date.split("/")[1], date.split("/")[0], date.split("/")[2]])
  if uk == "".join(uk[::-1]) and usa == "".join(usa[::-1]):
    return True
  return False

