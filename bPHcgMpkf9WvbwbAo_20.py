
def format_phone_number(lst):
  new = str(lst).strip(' ,[]').replace(', ', '')
  return "(" + new[0:3] + ") " + new[3:6] + "-" + new[6:]

