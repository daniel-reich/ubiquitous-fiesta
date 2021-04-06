
def license_plate(code, group):
  return translate(list(code), group, "")
​
def translate(code, group, newcode):
  if len(code) == 0:
    return newcode
  else:
    if len([char for char in newcode if char != "-"]) % group == 0 and len(newcode) > 0:
      newcode = "-" + newcode
    char = code.pop()
    char = char.upper()
    if char == "-":
      char = code.pop()
      char = char.upper()
    newcode = char + newcode
    return translate(code, group, newcode)

