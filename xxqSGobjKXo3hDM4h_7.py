
def ing_extractor(string):
 return [x for x in string.split() if x.lower().endswith('ing') and len(x)>5 and x!='string']

