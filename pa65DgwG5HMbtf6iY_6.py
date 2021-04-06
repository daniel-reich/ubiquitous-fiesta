
class player():
​
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    # complete function
​
    def get_age(self):
        return "{0} is age {1}".format(self.name, self.age)
    # complete function
​
    def get_height(self):
        return "{0} is {1}cm".format(self.name, self.height)
    # complete function
​
    def get_weight(self):
        return "{0} weighs {1}kg".format(self.name, self.weight)

