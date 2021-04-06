
def remove_leading_trailing(n):
  n = n.split(".")
  if len(n) == 1:
    return n[0].lstrip("0") if n[0].lstrip("0") != "" else "0"
  elif len(n) == 2:
    if n[1].rstrip("0") == "":
      return n[0].lstrip("0") if n[0].lstrip("0") != "" else "0"
    elif n[0].lstrip("0") == "":
      return "0" + "." + n[1].rstrip("0") if n[1].rstrip("0") != "" else "0"
    else:
      return n[0].lstrip("0") + "." + n[1].rstrip("0") if n[0].lstrip("0") + "." + n[1].rstrip("0") != "" else "0"

