
def pyramidal_string(string, _type):
  def is_triangle(n):
    i = 1
    while n > 0:
      n -= i
      i +=1
    if n == 0: return True, i-1
    return False, i-1
  if string == '': return []
  if not is_triangle(len(string))[0]: return 'Error!'
  lst = []
  layers = is_triangle(len(string))[1]
  if _type == 'REG':
    i = 1
    while i <= layers:
      ele = ' '.join([j for j in string[:i]])
      lst.append(ele)
      string = string[i:]
      i += 1
  else:
    i = layers
    while i >= 1:
      ele = ' '.join([j for j in string[:i]])
      lst.append(ele)
      string = string[i:]
      i -= 1
  return lst

