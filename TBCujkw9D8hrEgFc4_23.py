
from re import split
def validate_email(t):
  if t == "":
    return False
  t = [y.split(".") for y in t.split("@")]
  if len(t) == 1:
    return False
  return len(t[1]) == 2 and len(t[0]) >= 1 and "" not in t[0]

