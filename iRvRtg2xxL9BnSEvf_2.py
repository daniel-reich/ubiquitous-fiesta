
class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate
​
    def taste(self, var):
        a = var in self.like
        b = var in self.hate
        x = {
            (1, 0): " and loves it!",
            (0, 1): " and hates it!",
            (0, 0): "!"
        }[a, b]
        return "{} eats the {}{}".format(self.name, var, x)

