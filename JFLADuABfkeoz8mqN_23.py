
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
​
    def compare_age(self, other):
        diff = 'younger' 
        if self.age > other.age:
            diff = 'younger than'
        elif self.age < other.age:
            diff = 'older than'
        else:
            diff = 'the same age as'
        return '{} is {} me.'.format(other.name, diff)

