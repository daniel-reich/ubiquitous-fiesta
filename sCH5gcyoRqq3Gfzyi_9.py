
def valid_str_number(n): 
  try:
    return float(n) >= 0
  except ValueError:
    return False

