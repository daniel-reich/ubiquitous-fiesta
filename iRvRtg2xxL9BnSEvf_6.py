
class Person:
    def __init__(self,person_name,like,hate):
        self.person_name=person_name
        self.like=like
        self.hate=hate
    def taste(self,food_name):
        self.food_name=food_name
        if self.food_name in self.like:
            return "{} eats the {} and loves it!".format(self.person_name,self.food_name)
        elif self.food_name in self.hate:
            return "{} eats the {} and hates it!".format(self.person_name,self.food_name)
        else:
            return "{} eats the {}!".format(self.person_name,self.food_name)

