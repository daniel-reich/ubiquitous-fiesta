
def deep_sum(lst):
  def get_ints(string):
    digits = '0123456789'
    nums = []
    num = ''
    negative = False
    
    for l8r in string:
      if l8r in digits:
        num += l8r
      elif l8r == '-' and negative == False:
        if num != '':
          nums.append(int(num))
          num = ''
        num += l8r
        negative = True
      elif l8r == '-' and negative == True:
        if num != '-':
          nums.append(int(num))
        num = l8r
      else:
        if negative == True:
          if num != '-':
            nums.append(int(num))
          num = ''
          negative = False
        elif num != '':
          nums.append(int(num))
          num = ''
        else:
          continue
    
    if num != '':
      nums.append(int(num))
      num = ''
#   print(nums)
    return nums
  def denester(lst):
    l = str(lst).replace('[', '').replace(']','').split(', ')
    return [i for i in l if len(i) > 0 and i != '']
  
  #print(denester(lst))
  tr = [sum(get_ints(string)) for string in denester(lst)]
# print(tr)
  return sum(tr)

