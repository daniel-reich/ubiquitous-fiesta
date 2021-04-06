
def valid_str_number(n):
  try: 
    return isinstance(float(n), float)
  except:
    return False

