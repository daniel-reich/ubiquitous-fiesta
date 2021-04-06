
def postfix(expr):
  operators  = "*/+-";
  stack_expr  = [];
  values  = expr.split(" ");
  
  for value in values :
    if (value.isdigit()):
      stack_expr.append(value);
    elif (value in operators):
      b,a,op = (stack_expr.pop() , stack_expr.pop() , value)
      stack_expr.append(str(int(eval(a + op + b))));
    else :
      return "ooops the provided value isn't an operator or number";
      
  return int(stack_expr[0]);

