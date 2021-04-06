
def palindromic_date(date):
  parts = date.split('/')
  return parts[0] == parts[1] == parts[2][:2][::-1] == parts[2][2:][::-1]

