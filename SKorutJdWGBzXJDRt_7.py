
def greet_people(names):
  out=''
  if len(names)==1:
    return 'Hello'+' '+names[0]
  else:
    for i in range(len(names)):
      if i == len(names)-1:
        out+='Hello'+' '+names[i]
      else:
        out+='Hello'+' '+names[i]+', '
    return out

