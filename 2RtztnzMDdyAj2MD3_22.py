
def add(n1,n2):
  try:
    return str(int(n1) + int(n2))
  except TypeError:
    return "Invalid Operation"
  except ValueError:
    return "Invalid Operation"

