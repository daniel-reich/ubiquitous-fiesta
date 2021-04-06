
def valid_str_number(n):
  if n.count(".") == 0:
    return n.isdigit()
  elif n.count(".") == 1:
    n = n.split(".")
    n = "".join(n)
    return n.isdigit()
  else:
    return False

