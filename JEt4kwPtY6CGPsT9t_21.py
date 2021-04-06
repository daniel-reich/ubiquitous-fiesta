
def mathematical(exp, numbers):
  lst = []
  for i in numbers:
    op = exp[6]
    
    if(op is '+'):
      lst.append("f(%s)=%s" % (i, (i + int(exp[7]))))
    elif(op is '-'):
      lst.append("f(%s)=%s" % (i, (i - int(exp[7]))))
    elif(op is 'x'):
      lst.append("f(%s)=%s" % (i, (i * int(exp[7]))))
    elif(op is '^'):
      lst.append("f(%s)=%s" % (i, (i * i)))
    elif(op is '/'):
      lst.append("f(%s)=%s" % (i, int(i / int(exp[7]))))
    
  return (lst)

