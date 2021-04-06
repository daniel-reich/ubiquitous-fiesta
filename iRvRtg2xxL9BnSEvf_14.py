
class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate
​
    def taste(self, food):
        msg = self.name + ' eats the ' + food
        if food in self.like:
            return msg + ' and loves it!'
        if food in self.hate:
            return msg + ' and hates it!'
        return msg + '!'

