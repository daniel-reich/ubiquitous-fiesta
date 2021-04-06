
def get_birthday_cake(name, age):
    if age % 2 == 0:
        deco = "#"
    else:
        deco = "*"
    message = "{0} {1} Happy Birthday {2}! {1} {0}".format(deco, age, name)
    cake = [deco * len(message) for i in range(2)]
    cake.insert(1, message)
    return cake

