
def to_snake_case(string):
  i = 0
  result = ""
  while(i < len(string)):
    if(string[i] == string[i].upper()):
      result = result + "_" + string[i].lower()
    else:
      result = result + string[i]
    i = i + 1
  return(result)
def to_camel_case(string):
  i = 0
  result = ""
  while(i < len(string)):
    if(string[i] == "_"):
      result = result + string[i + 1].upper()
      i = i + 1
    else:
      result = result + string[i]
    i = i + 1
  return(result)
#Code By Cool Programmer

