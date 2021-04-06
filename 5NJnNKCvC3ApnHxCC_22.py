
def mubashir_function(a, b):
  def remove_zeros(num):
    num = str(num)
    if num != '0':
      return int(num.replace('0',''))
    else:
      return 0
  def reverser(num):
    return int(''.join(list(reversed(str(num)))))
  
  if len(str(remove_zeros(a))) != 1 or len(str(remove_zeros(b))) != 1:
    return reverser(min([a, b]))
  else:
    return remove_zeros(a) * remove_zeros(b)

