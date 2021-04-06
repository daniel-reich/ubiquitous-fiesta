
def ing_extractor(string):
  string = string.split()
  lst = []
  for i in string:
    if i.lower().endswith('ing') and any([j in i[:-3].lower() for j in 'aeiou*']):
      lst.append(i)
  return lst

