
def get_birthday_cake(name, age):
  sen = "# {0} Happy Birthday {1}! {0} #".format(age,name)
  arr = []
  if age % 2 == 0:
    arr.append('#'*len(sen))
    arr.append(sen)
    arr.append('#'*len(sen))
    
  else : 
    arr.append('*'*len(sen))
    arr.append(sen.replace('#','*'))
    arr.append('*'*len(sen))
  
  return arr

