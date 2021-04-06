
def valid_str_number(n):
  try:
    x = float(n)
    return True
  except ValueError:
    return False

