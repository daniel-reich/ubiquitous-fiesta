
def num_to_google(l):
  def f(y):
    r=''
    for x in y:
      if x=='0':return r*int(y[y.find('0')+1:])
      elif x=='5':r=r[:-1]+r[-1].upper()
      elif x=='6':r+='.'
      elif x=='7':r=r[0].swapcase()+r[1:]
      elif x=='8':r=r[::-1]
      elif x=='9':r=''
      else:r+=' gole'[int(x)]
    return r
  return''.join(map(f,map(str,l)))

