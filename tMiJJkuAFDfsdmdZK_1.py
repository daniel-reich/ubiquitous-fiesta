
def to_snake_case(txt):
  return "".join("_" + x.lower() if x.isupper() else x for x in txt)
​
def to_camel_case(txt):
  return txt[0] + txt.title().replace("_", "")[1:]

