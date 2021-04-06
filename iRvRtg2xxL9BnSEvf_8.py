
class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate
    def taste(self, food):
        if food in self.like:
            return str(self.name) + " eats the " + str(food) + " and loves it!"
        elif food in self.hate:
            return str(self.name) + " eats the " + str(food) + " and hates it!"
        else:
            return str(self.name) + " eats the " + str(food) + "!"
p1 = Person('Sam', ['ice cream'], ['carrots'])

