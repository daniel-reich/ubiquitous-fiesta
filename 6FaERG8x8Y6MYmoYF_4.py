
from collections import OrderedDict  
def dice_score(throw):
​
    def group_list(lst): 
        res =  [(el, lst.count(el)) for el in lst] 
        return list(OrderedDict(res).items()) 
​
    group = group_list(throw)
    total_score = 0
    for i in group:
        value = i[0]
        count = i[1]
        points = 0
        total_points = 0
​
        if value == 1 and count == 3:
            points = 1000
        elif value == 2 and count == 3:
            points = 200
        elif value == 3 and count == 3:
            points = 300
        elif value == 4 and count == 3:
            points = 400
        elif value == 5 and count == 3:
            points = 500
        elif value == 6 and count == 3:
            points = 600
        elif value == 1:
            points = 100
        elif value == 5:
            points = 50
        else:
            points = 0
    
​
        print('value:', value, 'count:', count, 'point value:', points)
​
        total_score += points
    
    return(total_score)

