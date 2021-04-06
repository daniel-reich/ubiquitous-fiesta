
def find_the_falsehoods(lst):
  null = []
  for x in lst:
    if bool(x) == False :
      null.append(x)
      
  return null

