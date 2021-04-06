
def valid_division(d):
  return "invalid" if int(d.split("/")[1])==0 else int(d.split("/")[0])%int(d.split("/")[1])==0

