
'''def basic_calculator(a, o, b):
    result = 0 
    if(O == "+"):
      return a + b
    elif(o == "-"):
      return a - b
    if(o == "/"):
      if (b==0):
        return null
    return a / b
    if(0 == "*"):
        return a * b
    return result'''
def basic_calculator(a,o,b):
    if(o == "+"):
        return (a+b)
    if(o == "-"):
        return (a-b)
    if(o == "*"):
        return (a*b)
    if(o=="/"):
        if (b==0):
            return (None)
        else:
            return (a/b)

