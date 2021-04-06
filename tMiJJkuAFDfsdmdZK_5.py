
def to_snake_case(txt):
  import re
  return "_".join(re.findall("^[a-z]+|[A-Z][a-z]*", txt)).lower()
  
​
def to_camel_case(txt):
  txt = "".join(word.title() for word in txt.split("_"))
  return txt.replace(txt[0], txt[0].lower())

