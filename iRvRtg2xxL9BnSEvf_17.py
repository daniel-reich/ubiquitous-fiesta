
class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate
​
    def taste(self, value):
        if value in self.like:
            return "{0} eats the {1} and loves it!".format(self.name,value)
        if value in self.hate:
            return "{0} eats the {1} and hates it!".format(self.name,value)
        else:
            return "{0} eats the {1}!".format(self.name,value)

