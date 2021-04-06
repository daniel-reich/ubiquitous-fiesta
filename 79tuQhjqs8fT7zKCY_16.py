
def postfix(expr):
  temp_list = []
  for c in expr.split():
    if c not in ['+', '-', '*', '/']:
      temp_list.append(c)
    else:
      if len(temp_list) > 1:
        y = temp_list.pop()
        x = temp_list.pop()
        temp_list.append(eval("{}{}{}".format(x,c,y)))
  return int(temp_list[0])

