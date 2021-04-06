
def is_authentic_skewer(s):
  
  l8rs = []
  seperators = set()
  seperator = ''
  print(s)
  for item in s:
    if item.isalpha() == True:
      l8rs.append(item)
      if seperator != '':
        seperators.add(seperator)
        seperator = ''
    elif item == '-':
      seperator += '-'
    else:
      print(item)
      return False
  
  if len(l8rs) == 0:
    return False
    
  if seperator != '':
    seperators.add(seperator)
  
  if len(list(seperators)) != 1:
    print(list(seperators))
    return False
  
  vowels = 'aeiou' + 'aeiou'.upper()
  
  for n in range(len(l8rs)):
    l8r = l8rs[n]
    even = n%2==0
    
    if even == True:
      if l8r in vowels:
        print('even-vowel')
        return False
    else:
      if l8r not in vowels:
        print('odd-con')
        return False
  
  if s.split(list(seperators)[0]) != l8rs:
    print(l8rs)
    return False
  
  return True

