
def greet_people(names):
  s=''
  for n in range(len(names)):
    s+='Hello '
    s+=names[n]
    if (n+1!=len(names)):
      s+=', '
  return s

