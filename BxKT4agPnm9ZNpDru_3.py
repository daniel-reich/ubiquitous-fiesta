
def zip_it(women, men):
  
  # Establishing Length of Lists:
  Women_Items = len(women)
  Men_Items = len(men)
  
  # Using Zip Function:
  Pairs = zip(women,men)
  Couples = tuple(Pairs)
  
  # Taking Out Mismatch in Length Branch
  if (Women_Items != Men_Items):
    return "sizes don't match"
  
  # When Lists Are Same Length
  else:
    return list(Couples)

