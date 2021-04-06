
def postfix(expr):
  l=expr.split(' ')
  stack=[]
  for i in l:
      if not i in ['+','-','*','/']:
          stack.append(i)
      else:
          k2=stack.pop()
          k1=stack.pop()
          if i=='+':
              stack.append(int(k1)+int(k2))
          elif i=='-':
              stack.append(int(k1)-int(k2))
          elif i=='*':
              stack.append(int(k1)*int(k2))
          elif i=='/':
              stack.append(int(k1)/int(k2))
  for i in stack:
      return int(i)

