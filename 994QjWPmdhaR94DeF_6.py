
def get_birthday_cake(name, age):
    ch = "#" if age%2==0 else "*"
    line = ch*(len(str(age))*2 + len(name) + 22)
    txt = "{0} {1} Happy Birthday {2}! {1} {0}".format(ch,age,name)
    return [line,txt,line]

