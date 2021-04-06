
def parse_roman_numeral(num):
  normal = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  special = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
  
  roman = num
  integers = []
  
  for char in special.keys():
    if char in roman:
      integers.append( special[char] )
      
  for char in special.keys():
    if char in roman:
      roman = roman[ : roman.index(char) ] + roman[ roman.index(char) + 2 :]
      
  for char in roman:
    integers.append( normal[char] )
    
  return sum(integers)

