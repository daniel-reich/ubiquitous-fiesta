
def get_birthday_cake(name, age):
    if age%2==0:
        m="# "+str(age)+" Happy Birthday "+name+"! " +str(age)+" #"
    else:
        m="* "+str(age)+" Happy Birthday "+name+"! "+str(age) +" *"
    return [len(m)*m[0], m ,len(m)*m[0]]

