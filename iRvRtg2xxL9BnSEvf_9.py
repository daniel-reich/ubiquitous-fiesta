
class Person:
    def __init__(self, person_name, like_list=[], hate_list=[]):
        self.person_name = person_name
        self.like_list = like_list
        self.hate_list = hate_list
    def taste(self, food_name):
        self.food = food_name
        if food_name in self.like_list:
            return '{} eats the {} and loves it!'.format(self.person_name, food_name)
        elif food_name in self.hate_list:
            return '{} eats the {} and hates it!'.format(self.person_name, food_name)
        else:
            return '{} eats the {}!'.format(self.person_name, food_name)

