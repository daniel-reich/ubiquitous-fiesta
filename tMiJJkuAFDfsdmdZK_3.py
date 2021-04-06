
def to_snake_case(txt):
  return "".join(c if c.islower() else "_"+c.lower() for c in txt)
  
def to_camel_case(txt):
  return txt[0] + "".join(w.title() for w in txt.split("_"))[1:]

