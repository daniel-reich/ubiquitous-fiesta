
vowels = 'aeiou'
​
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  code = ''
  code += surname(person['surname'])
  code += name(person['name'])
  code += year(person['dob'])
  code += month(person['dob'])
  code += day(person['dob'], person['gender'])
  return code
  
  
def surname(name):
  output = ''
  for c in name:
    if (is_consonant(c) and len(output) < 3):
      output += c.upper()
  
  for c in name:
    if (len(output) < 3):
      if (not is_consonant(c) and len(output) < 3):
        output += c.upper()
      
  for c in name:      
    if (len(output) < 3):
      while (len(output) < 3):
        output += 'X'
        
  return output
  
def name(s):
  output = ''
  for c in s:
    if (is_consonant(c)):
      output += c.upper()
  
  if (len(output) > 3):
    return output[0] + output[2:4]
  
  for c in s:
    if (len(output) < 3):
      if (not is_consonant(c) and len(output) < 3):
        output += c.upper()
      
  for c in s:     
    if (len(output) < 3):
      while (len(output) < 3):
        output += 'X'
        
  return output
  
def year(date):
  return date[-2:]
  
def month(date):
  s = date.split('/')
  return months[s[1]]
  
def day(date, gender):
  s = date.split('/')
  
  if (gender == 'M'):
    if (int(s[0]) < 10):
      return '0' + s[0]
    return s[0]
    
  return str(int(s[0]) + 40)
  
def is_consonant(s):
  return True if vowels.find(s.lower()) == -1 else False

