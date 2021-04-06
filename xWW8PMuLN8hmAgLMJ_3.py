
def postfix(expression):
  stack = expression.split(" ")[::-1];
  operations  ="+-*/";
  result_stack = [];
  while(len(stack) != 0):
    current = stack.pop();
    if (current in operations):
      a,b =  result_stack.pop() , result_stack.pop()
      result  = eval(b+ current + a);
      result_stack.append(str(result));
    elif (current.isdigit()) :
      result_stack.append(current)
    else :
      return "unknown provided value anyway";
  return float(result_stack[0]);

