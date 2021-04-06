
def ing_extractor(string):
  string = string.split(' ')
  myans = []
  v = ['a','e','i','o','u','A','E','I','O','U','*']
  for i in string:
    if len(i) > 4:
      if i[-3:].lower() == 'ing':
        for j in range(len(v)):
          if v[j] in i[:-3]: 
            myans.append(i)
            break
        
  return myans

