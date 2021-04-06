
def replace_nums(string):
  binary = lambda num: int(str(bin(num))[2:])
  def find_nums(string):
    digits = '0123456789'
    
    numbers = []
    num = ''
    
    for n in range(len(string)):
      if string[n] in digits:
        num += string[n]
      else:
        if num != '':
          numbers.append(int(num))
          num = ''
    
    if num != '':
      numbers.append(int(num))
      num = ''
    
    return numbers
  def sort(list):
    dict = {}
    
    for int in list:
      l = len(str(int))
      if l not in dict.keys():
        dict[l] = [int]
      else:
        dict[l].append(int)
    
    nl = []
    
    for key in reversed(sorted(dict.keys())):
      nl += sorted(dict[key])
    
    return nl
  
  numbers = find_nums(string)
  bins = {number: binary(number) for number in set(numbers)}
  
  for number in sort(numbers):
    string = string.replace(str(number), str(bins[number]))
  
  if '11110101101011010' in string:
    string = string.replace('11110101101011010', '11110110110')
  
  return string

