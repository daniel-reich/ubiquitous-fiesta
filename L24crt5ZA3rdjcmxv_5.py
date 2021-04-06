
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  def surname_coder(surname):
    vowels = 'A, E, I, O, U'.split(', ')
​
    cosonants_in_surname = []
​
    for l8r in surname:
      l8r = l8r.upper()
​
      if l8r not in vowels:
        cosonants_in_surname.append(l8r)
    
    l = len(cosonants_in_surname)
​
    coded = []
​
    if l >= 3:
      coded = cosonants_in_surname[:3]
    elif l < 3:
      for l8r in surname:
        l8r = l8r.upper()
​
        if l8r in vowels:
          cosonants_in_surname.append(l8r)
      
      ln = len(cosonants_in_surname)
​
      if ln >= 3:
        coded = cosonants_in_surname[:3]
      else:
​
        while ln < 3:
          cosonants_in_surname.append('X')
          ln = len(cosonants_in_surname)
        
        coded = cosonants_in_surname
    
    return coded
  def name_coder(name):
​
    vowels = 'a, e, i, o, u'.upper().split(', ')
​
    cosonants_in_name = []
​
    for l8r in name:
      l8r = l8r.upper()
​
      if l8r not in vowels:
        cosonants_in_name.append(l8r)
    
    l = len(cosonants_in_name)
    
    coded = []
    if l == 3:
      coded = cosonants_in_name
      print('coded')
​
    elif l > 3:
      coded = [cosonants_in_name[0], cosonants_in_name[2], cosonants_in_name[3]]
      print('moth')
​
    elif l < 3:
      nl = len(name)
      if nl >= 3:
        for l8r in name:
          l8r = l8r.upper()
​
          if l8r in vowels:
            cosonants_in_name.append(l8r)
        
        coded = cosonants_in_name
      elif nl < 3:
        print('hi')
        for l8r in name:
          l8r = l8r.upper()
​
          if l8r in vowels:
            cosonants_in_name.append(l8r)
          
        nl = len(cosonants_in_name)
​
        while nl < 3:
          cosonants_in_name.append('X')
          nl = len(cosonants_in_name)
        
        coded = cosonants_in_name
    
    
    return coded
  def dateofbirth_coder(dob, g):
    dob = dob.split('/')
​
    day = int(dob[0])
    month = dob[1]
    year = list(dob[2])
​
    months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H", "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
    ycode= '{y2}{y1}'.format(y2 = year[-2], y1 = year[-1])
    mcode = months[month]
​
    dcode = ''
    if g == 'M':
      if day < 10:
        dcode = '0' + str(day)
      else:
        dcode = str(day)
    elif g == 'F':
      dcode = str(day + 40)
​
    code = '{yc}{mc}{dc}'.format(yc = ycode, mc = mcode, dc = dcode)
​
    return code
  
  surname = person['surname']
  sc = surname_coder(surname)
  
  name = person['name']
  nc = name_coder(name)
  if len(nc) > 3:
    nc = nc[:3]
  gender = person['gender']
  dob = person['dob']
​
  dobcode = dateofbirth_coder(dob, gender)
​
  code = ''
​
  for item in sc:
    code += item
  for item in nc:
    code += item
  code += dobcode
​
  return code

