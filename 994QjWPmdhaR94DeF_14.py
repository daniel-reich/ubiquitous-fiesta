
def get_birthday_cake(name, age):
  if age % 2 != 0:
    a = "*"+" "+str(age)+" "+"Happy Birthday "+ str(name)+"!"+" "+str(age)+" "+"*"
    return ["*"*len(a),a,"*"*len(a)]
  else:
    a = "#"+" "+str(age)+" "+"Happy Birthday "+ str(name)+"!"+" "+str(age)+" "+"#"
    return ["#"*len(a),a,"#"*len(a)]

