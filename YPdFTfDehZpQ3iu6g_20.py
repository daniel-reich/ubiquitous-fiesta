
def roman_numerals(arg):
  result = 0
  ctr = 0
  
  if type(arg) == str:
    while len(arg) > 0:
      if ctr > 10:
        break
      ctr += 1
    
      if 'IV' in arg:
        result += 4*arg.count('IV')
        arg = arg.replace('IV','')
      if 'IX' in arg:
        result += 9*arg.count('IX')
        arg = arg.replace('IX','')
      elif 'I' in arg:
        result += arg.count('I')
        arg = arg.replace('I','')
      elif 'V' in arg:
        result += 5*arg.count('V')
        arg = arg.replace('V','')
      elif 'IX' in arg:
        result += 9*arg.count('IX')
        arg = arg.replace('IX','')
      elif 'XC' in arg:
        result += 90*arg.count('XC')
        arg = arg.replace('XC','')
      elif 'XL' in arg:
        result += 40*arg.count('XL')
        arg = arg.replace('XL','')
      elif 'X' in arg:
        result += 10*arg.count('X')
        arg = arg.replace('X','')
      elif 'L' in arg:
        result += 50*arg.count('L')
        arg = arg.replace('L','')
      elif 'C' in arg:
        result += 100*arg.count('C')
        arg = arg.replace('C','')
      elif 'D' in arg:
        result += 500*arg.count('D')
        arg = arg.replace('D','')
      elif 'M' in arg:
        result += 1000*arg.count('M')
        arg = arg.replace('M','')
    return result
  else:
    result = ''
    while arg > 0:
      if ctr > 10:
        break
      ctr += 1
      if arg > 1000:
        result += 'M'
        arg -= 1000
      elif arg > 100:
        result += 'C'
        arg -= 100
      elif arg > 50:
        result += 'L'
        arg -= 50
      elif arg > 10:
        result += 'X'
        arg -= 10
      elif arg > 5:
        result += 'V'
        arg -= 5
      elif arg > 0:
        result += 'I'
        arg -= 1
    if 'IIII' in result:
      result = result.replace('IIII','IV')
    return result

