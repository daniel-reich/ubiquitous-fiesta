
def arithmetic_operation(n):
  x,op,y = n.split()
  x,y = int(x), int(y)
  return x+y if op=='+' else x*y if op=='*' else x-y if op=='-' else x/y if op=='/' and y != 0 else -1

