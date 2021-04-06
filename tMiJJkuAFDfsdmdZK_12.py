
def to_snake_case(txt):
  return ''.join("_"+x.lower() if x.isupper() else x for x in txt)
​
def to_camel_case(txt):
  return txt.split("_")[0]+''.join(x.title()for x in txt.split("_")[1:])

