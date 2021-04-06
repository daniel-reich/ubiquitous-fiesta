
def halloween(dt):
  year,month,day = dt.split("/")
  if month == "10" and day == "31":
    return "Bonfire toffee"
  else:
    return "toffee"

