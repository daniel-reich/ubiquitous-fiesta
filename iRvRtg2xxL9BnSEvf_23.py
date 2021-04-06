
class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate
​
    def taste(self, food):
        fullTxt = ["{} eats the {}"]
​
        if food in self.like:
            fullTxt.append('and loves it')
        elif food in self.hate:
            fullTxt.append('and hates it')
​
        return (' '.join(fullTxt) + '!').format(self.name, food)

