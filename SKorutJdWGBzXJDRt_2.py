
def greet_people(names):
  ending = ""
  for nam in names:
    ending += ("Hello "+nam + ", ")
    
  return ending[:-2]

