
def zip_it(women,men):
  if len(women) != len(men):
    return 'sizes don\'t match'
  else:
    return list(zip(women, men))

