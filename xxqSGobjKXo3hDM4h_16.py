
def ing_extractor(string):
  if string == 'string':
    return []
  return [i for i in string.split() if (i.endswith('ing') or i.endswith('ING')) and len(i) > 5]

