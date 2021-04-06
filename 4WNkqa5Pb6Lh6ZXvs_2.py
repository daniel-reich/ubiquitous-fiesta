
def evaluate_polynomial(poly, num):
  out=''
  if  len([c for c in poly if c=='('])!=len([c for c in poly if c==')']) or \
  sum([1 for s in ['#','$','//','%','|','&','print'] if s in poly])>0 or len(poly)==0:
    return 'invalid'
  for i in range(len(poly)):
    if poly[i]== 'x':
      if i< len(poly)-1 and i>0:
        if poly[i-1].isnumeric():
          if poly[i+1].isnumeric() or poly[i+1]=='(':
            out+='*' + str(num) + '*'
          else:
            out+='*' + str(num)
        elif (poly[i+1].isnumeric() or poly[i+1]=='(') and not poly[i-1].isnumeric():
          out+=str(num) + '*'
        else:
          out+=str(num)
      else:
        if i==0:
          if (i+1 < len(poly)-1):
            if (poly[i+1].isnumeric() or poly[i+1]=='('):
              out+=str(num) + '*'
            else:
              out+=str(num)
          else:
            out+=str(num)
        else:
          if(i-1 >=0):
            if poly[i-1].isnumeric() or poly[i-1]==')':
              out+='*' + str(num)
            else:
              out+= str(num)
          else:
            out+= str(num)
​
    else:
      if (poly[i]=='^'):
        out+='**'
      elif (poly[i].isnumeric()):
        if (i+1 < len(poly)-1):
          if poly[i+1]=='(':
            out+=poly[i]+'*'
          else:
            out+=poly[i]
        else:
          out+=poly[i]
      else:
        out+=poly[i]
  return round(eval(out))

