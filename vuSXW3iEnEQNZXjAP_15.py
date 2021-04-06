
def create_square(length):
  if type(length) != int:
    return "" 
  arr = []
  for i in range(length):
    if i == 0:
      arr.append('#'*length)
    elif i == length-1:
      arr.append('\n' + '#'*length)
    else : arr.append('\n'+'#' + ' '*(length-2) + '#')
  return "".join(arr)

