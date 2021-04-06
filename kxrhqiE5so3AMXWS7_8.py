
def get_number_of_apples(n, p):
  apples = int(n * (100 - int(p[:-1])) / 100)
  return "The children didn't get any apples" if not apples else apples

