
def greet_people(names):
  if len(names)==0:
    return ""
  txt="Hello "+names[0]
  for i in range(1,len(names)):
    txt=txt+", Hello "+names[i]
  return txt

