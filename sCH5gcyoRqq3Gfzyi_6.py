
def valid_str_number(n):
  try: 
    bool(float(n))
  except ValueError:
    return False
  return True

