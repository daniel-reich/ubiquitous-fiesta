
def get_birthday_cake(name, age):
    s = '{} Happy Birthday {}! {}'.format(age, name, age)
    edge = '*' if age % 2 else '#'
    return [edge * (len(s) + 4), edge + ' ' + s + ' ' + edge,
            edge * (len(s) + 4)]

