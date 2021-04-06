
def to_snake_case(txt):
  from string import ascii_uppercase as up
  result = ""
  for char in txt:
    result += char if not char in up else "_"+char.lower()
  return result
  
​
def to_camel_case(txt):
  from string import capwords
  result = capwords(txt,"_").replace("_","")
  return result[0].lower()+result[1:]

