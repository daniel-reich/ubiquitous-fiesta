
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
​
    def compare_age(self, other):
        if other.age > self.age:
            return "{} is older than me.".format(other.name)
        elif other.age < self.age:
            return "{} is younger than me.".format(other.name)
        return "{} is the same age as me.".format(other.name)

