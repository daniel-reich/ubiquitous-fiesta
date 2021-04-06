
def valid_division(d):
  return "invalid" if "0" in d[-1] else eval(d) == int(d.split("/")[0]) // int(d.split("/")[-1])

