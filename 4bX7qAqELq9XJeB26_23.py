
def to_camel_case(txt):
  return "".join(wd if wd[0].islower and i == 0 else wd.title() 
           for i, wd in enumerate("".join(txt.replace("-", "_")).split("_"))) if txt else ""

