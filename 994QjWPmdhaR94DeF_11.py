
def get_birthday_cake(name, age):
    line2 = " {0} Happy Birthday {1}! {0} ".format(age, name)
    tot_len = len(line2) + 2
    cake = []
    for line in range(3):
        if line == 0 or line == 2:
            if age % 2 == 0:
                cake.append("#" * tot_len)
            else:
                cake.append("*" * tot_len)
        else:
            if age % 2 == 0:
                cake.append("#" + line2 + "#")
            else:
                cake.append("*" + line2 + "*")
    return cake

