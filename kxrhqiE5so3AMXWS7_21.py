
def get_number_of_apples(n, p):
  return "The children didn't get any apples" if not n or p == "100%" else int(n - int(p[:-1]) * n / 100)

