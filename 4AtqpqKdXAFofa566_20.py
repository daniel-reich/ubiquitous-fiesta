
def remove_leading_trailing(n):
  n = n.lstrip("0")
  if "." in n:
    n = n.rstrip("0").rstrip(".")
  if not n or n[0] == ".":
    n = "0" + n
  return n

