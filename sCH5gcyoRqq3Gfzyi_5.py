
def valid_str_number(n):
  try:
    check = float(n)
    return True
  except ValueError:
    return False

