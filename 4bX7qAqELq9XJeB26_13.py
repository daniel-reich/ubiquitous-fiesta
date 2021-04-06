
def to_camel_case(txt):
  a = txt.split("-") if "-" in txt else txt.split("_")
  return "".join([v.capitalize() if i > 0 else v for i,v in enumerate(a)])

