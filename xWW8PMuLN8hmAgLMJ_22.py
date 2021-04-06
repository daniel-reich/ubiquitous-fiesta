
def postfix(expression):
​
  result = expression.split()
  operators = '+ - * / ** %'.split()
​
  while len(result) > 1:
  
    for n in range(0, len(result)):
      item = result[n]
      try:
        test = int(item)
      except ValueError:
        if item not in operators:
          return 'UNKNOWN OPERATOR!! {o}'.format(o = item)
        
        try:
          n1 = int(result[n - 2])
          n2 = int(result[n - 1])
        except IndexError:
          return n1, n2, n-2, n-1, result
        
        expression = eval('{n1} {o} {n2}'.format(n1 = n1, o = item, n2 = n2))
​
        nr = result[:n-2] + [expression] + result[n + 1:]
​
        result = nr
        
        break
  
  return result[0]

