
def validate(s):
  import re
  return re.findall(r'^[\+]?[1]?[-\.\s\/]?\(?\d{3}\)?[-\.\s\\/)]?\d{3}[-\.\s\/]?\d{4}', s) != []

