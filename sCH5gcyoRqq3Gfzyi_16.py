
def valid_str_number(n):
  try:
    float(n)
    return True
  except ValueError:
    return False

