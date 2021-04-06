
def get_drink_ID(flavor, ml):
  addition = ml.replace('ml','')
  words = flavor.split(' ')
  emptystring = ""
  for eachword in words:
    emptystring += eachword[0:3]
  return '{}{}'.format(emptystring.upper(),addition)

