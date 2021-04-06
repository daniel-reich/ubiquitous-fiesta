
def valid_str_number(n):
  try:
    n_string = str(n)
    if '.' in n_string:
      float(n_string)
    else:
      int(n_string)
  except (SyntaxError, ValueError):
    return False
  return True

