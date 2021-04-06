
def greater_permutation(expr, num):
  result = []
  expressions = []
  for x in range(0, len(num)):
    expression = expr
    a = num[x]
    del(num[x])
    for x in range(0, len(num)):
      expression = expr
      if x == 0:
        b = num[0]
        c = num[1]
      else:
        c = num[0]
        b = num[1]
      n = eval(expression, {"a":a, "b":b, "c":c})
      result.append(n)
      expression = expression.replace("a", str(a))
      expression = expression.replace("b", str(b))
      expression = expression.replace("c", str(c))
      expressions.append(expression)
    num.insert(x-1, a)
  zipped_pairs = zip(result, expressions)   
  z = [x for _, x in sorted(zipped_pairs, reverse = True)]
  result = sorted(result, reverse = True)
  if str(round(result[0], 2))[-1] != "0":
    string = z[0] + " = " + str(round(result[0], 2))
  else:
    string = z[0] + " = " + str(int(result[0]))
  return string

