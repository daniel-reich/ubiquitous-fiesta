
import re
​
def time_to_eat(current_time):
    pattern=r'(\d+):(\d\d) (\w)\.\w\.'
​
    matches=re.findall(pattern,current_time)
    bf=7
    lunch=12
    dinner=7
    if (matches[0][2]=='p'):        
        if(int(matches[0][1])==00  and int(matches[0][0])<7 ):
            next_meal_hr=7-int(matches[0][0])
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        if(int(matches[0][1])==00  and int(matches[0][0])==12 ):
            next_meal_hr=int(matches[0][0])-7
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        else:
            if(int(matches[0][0])==12):
                next_meal_hr=12-6
            if(int(matches[0][0])<7):
                next_meal_hr=6-int(matches[0][0])
            if(int(matches[0][0])>7):
                next_meal_hr=18-int(matches[0][0])    
​
            next_meal_min=60-int(matches[0][1])
            return [next_meal_hr,next_meal_min]
    if (matches[0][2]=='a' and int(matches[0][0])<12 and int(matches[0][0])>7):
        if(int(matches[0][1])==0 ):
            next_meal_hr=12-int(matches[0][0])
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
​
        else:
            next_meal_hr=11-int(matches[0][0])
            next_meal_min=60-int(matches[0][1])
            return [next_meal_hr,next_meal_min]
​
    if (matches[0][2]=='a'):
        if(int(matches[0][1])==0  and int(matches[0][0])<7 ):
            next_meal_hr=7-int(matches[0][0])
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        if(int(matches[0][1])==0  and int(matches[0][0])==12 ):
            next_meal_hr=12-5
            next_meal_min=0
            return [next_meal_hr,next_meal_min]
        else:
            if(int(matches[0][0])==12):
                next_meal_hr=12-6
            if(int(matches[0][0])<7):
                next_meal_hr=6-int(matches[0][0])
            next_meal_min=60-int(matches[0][1])
            return [next_meal_hr,next_meal_min]

