
def eng2nums(s):
  ones = ['zero','one','two','three','four','five','six','seven','eight','nine',
  'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
  'eighteen','nineteen']
  tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
  fin = 0
  for i in s.split():
    if i in ones:
      fin+=ones.index(i)
    elif i in tens:
      fin+=(tens.index(i)+2)*10
    else:
      fin*=100
  return fin

