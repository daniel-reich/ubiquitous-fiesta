
def format_phone_number(lst):
  phone = ""
  phone += "("
  for i in lst[:3]:
    phone += str(i)
  phone += ") "
  for i in lst[3:6]:
    phone += str(i)
  phone += "-"
  for i in lst[6:]:
    phone += str(i)
  return phone

