
def worded_math(equ):
  values_s = {'one':1,'two':2,'zero':0}
  values_t = {1:'One',2:'Two',0:'Zero'}
  math_list = equ.split(' ')
  operation = math_list[1].lower()
  if operation == 'plus':
    return values_t[values_s[math_list[0].lower()] + values_s[math_list[2].lower()]]
  else:
    return values_t[values_s[math_list[0].lower()] - values_s[math_list[2].lower()]]

