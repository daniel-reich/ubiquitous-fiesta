
class Employee:
    def __init__(self,name,**info):
        self.name,self.lastname = name.split(' ')
        for i in info:
            setattr(self,i,info[i])

