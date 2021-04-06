
def greatest_impact(lst):
  # lst in format: [Mood, Weather, Meals, Sleep]
​
    Weather, Meals, Sleep=[], [], []    
    mood = [Weather, Meals, Sleep]
    mo = [ "Weather", "Meals", "Sleep"]
    for i in range(len(mood)):
        for j in range(len(lst)):
            mood[i].append(lst[j][i+1])
    sm = [sum(Weather),sum(Meals)*10/3,sum(Sleep)]    
    if sm.count(min(sm))>1:return'Nothing'
    else:return mo[sm.index(min(sm))]

