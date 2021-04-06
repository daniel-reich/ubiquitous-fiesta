
def to_snake_case(txt):
  result = ""
  for i in txt:
    if i.isupper():
      result += "_" + i.lower()
    else:
      result += i
  return result
​
def to_camel_case(txt):
  under = False
  result = ""
  for i in txt:
    if under:
      result += i.upper()
      under = False
    elif i == "_":
      under = True
    else:
      result += i
  return result

