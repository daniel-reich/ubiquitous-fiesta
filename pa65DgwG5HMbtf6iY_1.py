
class player():
​
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_age(self):
        return self.name + ' is age ' + str(self.age)
    
    def get_height(self):
        return self.name + ' is ' + str(self.height) + 'cm'
    
    def get_weight(self):
        return self.name + ' weighs ' + str(self.weight) + 'kg'

