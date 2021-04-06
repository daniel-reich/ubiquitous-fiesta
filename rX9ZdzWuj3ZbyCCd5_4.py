
def multiply_by_11(s):
  def integerify(string, index = 0):
    if index == len(string):
      return 0
    else:
      dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
      return dic[string[index]] * 10 ** (len(string) - 1 - index) + integerify(string, index + 1)
  def mult_by_11(integer, times = 1, add = None):
    if times == 11:
      return integer
    else:
      if add == None:
        add = integer
      return mult_by_11(integer + add, times + 1, add)
  
  integer = integerify(s)
  mult11 = mult_by_11(integer)
  
  return str(mult11)

